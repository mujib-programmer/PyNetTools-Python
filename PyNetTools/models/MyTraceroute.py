#!/usr/bin/python


import optparse, sys, socket

from PyQt4 import QtCore, QtGui

class MyTraceroute(QtCore.QThread):

    # Konstruktor untuk class MyTraceroute
    def __init__(self):
        QtCore.QThread.__init__(self)

        self.icmp = socket.getprotobyname('icmp')
        self.udp = socket.getprotobyname('udp')

    # method yang menangani inisiasi data awal untuk traceroute
    # harus dijalankan sebelum menjalankan method run
    def initialize(self, dest_name, port, max_hops):
        self.dest_name = dest_name
        self.dest_addr = socket.gethostbyname(self.dest_name)
        self.port = port
        self.max_hops = max_hops

    # method untuk membuat socket
    def create_sockets(self, ttl):
        """
        Mengatur socket yang diperlukan untuk traceroute.
        Kita memerlukan soket penerima dan socket pengirim
        """
        recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, self.icmp)
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, self.udp)
        send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        return recv_socket, send_socket

    # method ini akan dieksekusi saat class ini dijalankankan dalam thread
    def run(self):
        # beritahukan bahwa traceroute akan dimulai
        self.print_start()

        # inisiasi data awal time to life
        # ttl akan bertambah seiring semakin banyaknya hops yang telah dikunjungi
        ttl = 1
        while True:
            recv_socket, send_socket = self.create_sockets(ttl)
            recv_socket.bind(("",self. port))
            send_socket.sendto("", (self.dest_name, self.port))
            curr_addr = None
            curr_name = None
            try:
                # socket.recvfrom() mengembalikan (data, address), tetapi kita hanya peduli dengan yang terakhir
                _, curr_addr = recv_socket.recvfrom(512)
                curr_addr = curr_addr[0]  # address diberikan sebagai tuple
                try:
                    curr_name = socket.gethostbyaddr(curr_addr)[0]
                except socket.error:
                    curr_name = curr_addr
            except socket.error:
                pass
            finally:
                send_socket.close()
                recv_socket.close()

            if curr_addr is not None:
                curr_host = "%s\t(%s)" % (curr_name, curr_addr)
            else:
                curr_host = "*"

            respon = "%d\t%s" % (ttl, curr_host)
            self.emit(QtCore.SIGNAL("updateResponTracerouteTextEdit(QString)"), respon)

            ttl += 1
            if curr_name == self.dest_addr or ttl > self.max_hops:
                break

        # beritahukan bahwa traceroute telah selesai
        self.print_exit()

    # method untuk menampilkan data ke GUI saat traceroute sudah dimulai
    def print_start(self):
        # beritahukan bahwa proses traceroute akan dimulai
        respon = "Traceroute sedang diproses ...."
        self.emit(QtCore.SIGNAL("updateInfoResponTracerouteLabel(QString)"), respon)


        respon = "\nPYTHON-TRACEROUTE %s (%s): maks %d hops" % (self.dest_name, self.dest_addr, self.max_hops)
        self.emit(QtCore.SIGNAL("updateResponTracerouteTextEdit(QString)"), respon)

        self.emit(QtCore.SIGNAL("updateResponTracerouteTextEdit(QString)"), "----------------------------------------------------------------")

    # method untuk menampilkan data ke GUI saat traceroute sudah selesai
    def print_exit(self):
        respon = "Traceroute selesai dijalankan"
        self.emit(QtCore.SIGNAL("updateInfoResponTracerouteLabel(QString)"), respon)

        # cetak output di form
        respon = "\n----%s PYTHON TRACEROUTE selesai dijalankan ----" % (self.dest_name)
        self.emit(QtCore.SIGNAL("updateResponTracerouteTextEdit(QString)"), respon)

