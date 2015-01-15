#!/usr/bin/env python
# coding: utf-8

"""
    Implementasi ping dengan murni bahasa Python menggunakan raw socket

    Sebagai catatan bahwa pesan ICMP hanya bisa di kirimkan melalui proses yang di jalankan oleh root
"""

import os, sys, socket, struct, select, time, signal

from PyQt4 import QtCore, QtGui

# Mengatasi perbedaan timer di windows dan linux
if sys.platform == "win32":
    # di windows, timer terbaik adalah time.clock()
    default_timer = time.clock
else:
    # di kebanyakan platform lainnya timer terbaik adalah time.time()
    default_timer = time.time


# Parameter ICMP
ICMP_ECHOREPLY = 0      # Echo balasan (per RFC792)
ICMP_ECHO = 8           # Echo permintaan (per RFC792)
ICMP_MAX_RECV = 2048    # Maksimum ukuran buffer yang datang

MAX_SLEEP = 1000


def calculate_checksum(source_string):
    """
    Porting dari fungsionalitas in_cksum() di code ping.c
    Idealnya ia akan diterapkan pada string sebagai kumpulan integer 16-bit
    (dipaketkan oleh host), tetapi ini bekerja dengan baik
    Data network adalah big-endian, host umumnya little-endian
    """
    countTo = (int(len(source_string) / 2)) * 2
    sum = 0
    count = 0

    # Menangani bytes berpasangan (di-decode sebagai short int)
    loByte = 0
    hiByte = 0
    while count < countTo:
        if (sys.byteorder == "little"):
            loByte = source_string[count]
            hiByte = source_string[count + 1]
        else:
            loByte = source_string[count + 1]
            hiByte = source_string[count]
        sum = sum + (ord(hiByte) * 256 + ord(loByte))
        count += 2

    # Menangani byte terakhir jika ada (byte bilangan-ganjil)
    # Endianness harusnya relevan dalam kasus ini
    if countTo < len(source_string): # mengecek untuk panjang ganjil
        loByte = source_string[len(source_string) - 1]
        sum += ord(loByte)

    sum &= 0xffffffff # Batasi jumlah menjadi 32 bit (varian dari ping.c, yang mana
                      # menggunakan signed int, tapi overflow tampaknya tidak mungkin dalam ping)

    sum = (sum >> 16) + (sum & 0xffff)    # Tambahkan high 16 bits ke low 16 bits
    sum += (sum >> 16)                    # Tambahkan carry dari atas (jika ada)
    answer = ~sum & 0xffff                # Invert dan potong menjadi 16 bit
    answer = socket.htons(answer)

    return answer

class MyPing(QtCore.QThread):

    # konstruktor untuk objek MyPing
    def __init__(self):
        # Inisiasi objek QThread agar objek dari MyPing bisa dijalankan sebagai thread
        QtCore.QThread.__init__(self)

    #--------------------------------------------------------------------------

    # method yang menangani inisiasi data-data awal yang diperlukan untuk melakukan ping
    # harus dijalankan sebelum menjalankan method run
    def initialize(self, destination, timeout=1000, packet_size=55, own_id=None, count=None):
        self.destination = destination
        self.timeout = timeout
        self.packet_size = packet_size
        self.count = count

        if own_id is None:
            self.own_id = os.getpid() & 0xFFFF
        else:
            self.own_id = own_id

        try:
            self.dest_ip = socket.gethostbyname(self.destination)
        except socket.gaierror as e:
            self.print_unknown_host(e)
            sys.exit(-1)
        else:
            self.print_start()

        self.seq_number = 0
        self.send_count = 0
        self.receive_count = 0
        self.min_time = 999999999
        self.max_time = 0.0
        self.total_time = 0.0

    # method untuk menampilkan data saat ping sudah dimulai
    def print_start(self):

        respon = "Ping sedang diproses ...."
        self.emit(QtCore.SIGNAL("updateInfoResponPingLabel(QString)"), respon)

        respon = "\nPYTHON-PING %s (%s): %d data bytes" % (self.destination, self.dest_ip, self.packet_size)
        self.emit(QtCore.SIGNAL("updateResponPingTextEdit(QString)"), respon)

        self.emit(QtCore.SIGNAL("updateResponPingTextEdit(QString)"), "----------------------------------------------------------------")

    # method untuk menampilkan data saat ping mengembalikan error host tidak diketahui
    def print_unknown_host(self, e):
        respon = "\nPYTHON-PING: Host tidak diketahui: %s (%s)\n" % (self.destination, e.args[1])
        self.emit(QtCore.SIGNAL("updateResponPingTextEdit(QString)"), respon)

    # method untuk menampilkan data saat ping telah sukses dilaksanakan
    def print_success(self, delay, ip, packet_size, ip_header, icmp_header):
        if ip == self.destination:
            from_info = ip
        else:
            from_info = "%s (%s)" % (self.destination, ip)

        """print("%d bytes from %s: icmp_seq=%d ttl=%d time=%.1f ms" % (
            packet_size, from_info, icmp_header["seq_number"], ip_header["ttl"], delay)
        )"""


        respon = "%d bytes dari %s: icmp_seq=%d ttl=%d time=%.1f ms" % (packet_size, from_info, icmp_header["seq_number"], ip_header["ttl"], delay)
        self.emit(QtCore.SIGNAL("updateResponPingTextEdit(QString)"), respon)

    # method untuk menampilkan data saat proses ping gagal
    def print_failed(self):
        respon = "Request timed out."
        self.emit(QtCore.SIGNAL("updateResponPingTextEdit(QString)"), respon)

    # method untuk menampilkan data ke GUI saat ping sudah selesai
    def print_exit(self):

        respon = "Ping telah selesai dijalankan"
        self.emit(QtCore.SIGNAL("updateInfoResponPingLabel(QString)"), respon)

        # cetak output di form
        respon = "\n----%s PYTHON PING Statistics----" % (self.destination)
        self.emit(QtCore.SIGNAL("updateResponPingTextEdit(QString)"), respon)

        lost_count = self.send_count - self.receive_count
        lost_rate = float(lost_count) / self.send_count * 100.0

        respon = "%d paket dikirimkan, %d paket diterima, %0.1f%% paket hilang" % (self.send_count, self.receive_count, lost_rate)
        self.emit(QtCore.SIGNAL("updateResponPingTextEdit(QString)"), respon)

        if self.receive_count > 0:

            respon = "pulang-pergi (ms)  min/rata-rata/maks = %0.3f/%0.3f/%0.3f" % (self.min_time, self.total_time / self.receive_count, self.max_time)
            self.emit(QtCore.SIGNAL("updateResponPingTextEdit(QString)"), respon)


    #--------------------------------------------------------------------------

    # method ini akan dijalankan saat object dari class ini dijalankan sebagai thread
    def run(self, count=None, deadline=None):

        """
        Kirim dan terima ping dalam sebuah perulangan. Berhenti setelah jumlah ping tercapai atau mencapai deadline.
        """
        while True:
            delay = self.do()

            self.seq_number += 1

            if self.count and self.seq_number >= self.count:
                    break

            if deadline and self.total_time >= deadline:
                break

            if delay == None:
                delay = 0

            # Jeda untuk sisa periode MAX_SLEEP (jika ada)
            if (MAX_SLEEP > delay):
                time.sleep((MAX_SLEEP - delay) / 1000.0)

        self.print_exit()


    # method untuk melakukan satu kali ping dan menerima respon
    # dijalankan oleh method run() dalam sebuah perulangan sebanyak ping yang diinginkan
    def do(self):
        """
        Mengirim satu ICMP ECHO_REQUEST dan menerima respon sampai self.timeout
        """
        try:
            # Kita bisa menggunakan UDP disini, tapi itu harus jelas
            current_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname("icmp"))
        except socket.error, (errno, msg):
            if errno == 1:
                # Operasi tidak di ijinkan -  tambahkan informasi lebih lanjut
                etype, evalue, etb = sys.exc_info()
                evalue = etype(
                    "%s - Perhatikan bahwa pesan ICMP hanya dapat dikirim melalui proses yang dijalankan oleh root." % evalue
                )
                raise etype, evalue, etb

            raise # meningkatkan error aslinya

        send_time = self.send_one_ping(current_socket)
        if send_time == None:
            return
        self.send_count += 1

        receive_time, packet_size, ip, ip_header, icmp_header = self.receive_one_ping(current_socket)
        current_socket.close()

        if receive_time:
            self.receive_count += 1
            delay = (receive_time - send_time) * 1000.0
            self.total_time += delay
            if self.min_time > delay:
                self.min_time = delay
            if self.max_time < delay:
                self.max_time = delay

            self.print_success(delay, ip, packet_size, ip_header, icmp_header)
            return delay
        else:
            self.print_failed()

    # method yang digunakan untuk mengirimkan permintaan satu kali ping
    # dijalankan dalam method do()
    def send_one_ping(self, current_socket):
        """
        Kirim satu ICMP ECHO_REQUEST
        """
        # Headernya adalah type (8), code (8), checksum (16), id (16), sequence (16)
        checksum = 0

        # Membuat dummy header dengan cheksum 0.
        header = struct.pack(
            "!BBHHH", ICMP_ECHO, 0, checksum, self.own_id, self.seq_number
        )

        padBytes = []
        startVal = 0x42
        for i in range(startVal, startVal + (self.packet_size)):
            padBytes += [(i & 0xff)]  # Menjaga chars dalam jangkauan 0-255
        data = bytes(padBytes)

        # Hitung checksum pada data dan header dummy
        checksum = calculate_checksum(header + data) # Checksum adalah dalam urutan jaringan

        # Sekarang kita memiliki cheksum yang tepat, kami menempatkannya didalam. Ini hanya lebih mudah
        # untuk membuat header baru dari pada menempatkannya ke dummy.
        header = struct.pack(
            "!BBHHH", ICMP_ECHO, 0, checksum, self.own_id, self.seq_number
        )

        packet = header + data

        send_time = default_timer()

        try:
            current_socket.sendto(packet, (self.destination, 1)) # Nomor port tidak relevan untuk ICMP
        except socket.error as e:
            print("General failure (%s)" % (e.args[1]))
            current_socket.close()
            return

        return send_time

    # method yang digunakan untuk menerima respon satu kali ping
    # yang telah dikirim oleh method send_one_ping(current_socket)
    # dijalankan dalam method do()
    def receive_one_ping(self, current_socket):
        """
        Menerima ping dari socket. timeout = dalam ms
        """
        timeout = self.timeout / 1000.0

        while True: # Mengulang sampai paket diterima atau mencapai timeout
            select_start = default_timer()
            inputready, outputready, exceptready = select.select([current_socket], [], [], timeout)
            select_duration = (default_timer() - select_start)
            if inputready == []: # timeout
                return None, 0, 0, 0, 0

            receive_time = default_timer()

            packet_data, address = current_socket.recvfrom(ICMP_MAX_RECV)

            icmp_header = HeaderInformation(
                names=[
                    "type", "code", "checksum",
                    "packet_id", "seq_number"
                ],
                struct_format="!BBHHH",
                data=packet_data[20:28]
            )

            if icmp_header["packet_id"] == self.own_id: # Paket kita
                ip_header = HeaderInformation(
                    names=[
                        "version", "type", "length",
                        "id", "flags", "ttl", "protocol",
                        "checksum", "src_ip", "dest_ip"
                    ],
                    struct_format="!BBHHHBBHII",
                    data=packet_data[:20]
                )
                packet_size = len(packet_data) - 28
                ip = socket.inet_ntoa(struct.pack("!I", ip_header["src_ip"]))
                return receive_time, packet_size, ip, ip_header, icmp_header

            timeout = timeout - select_duration
            if timeout <= 0:
                return None, 0, 0, 0, 0


""" Penyimpanan sederhana untuk menerima informasi header IP dan ICMP """
class HeaderInformation(dict):

    def __init__(self, names, struct_format, data):
        unpacked_data = struct.unpack(struct_format, data)
        dict.__init__(self, dict(zip(names, unpacked_data)))
