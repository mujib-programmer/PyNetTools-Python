#!/usr/bin/python

import subprocess

from PyQt4 import QtCore

class MyNslookup(QtCore.QThread):

    # Konstruktor untuk class MyTraceroute
    def __init__(self):
        # buat objek QThread yang merupakan parent dari class ini
        QtCore.QThread.__init__(self)



    # method yang menangani inisiasi data awal untuk nslookup
    # harus dijalankan sebelum menjalankan method run
    def initialize(self, tujuan):
        self.tujuan = tujuan

    # method ini akan dieksekusi saat class ini dijalankankan dalam thread
    def run(self):
        # beritahukan bahwa traceroute akan dimulai
        self.print_start()

        # perintah di linux yang akan digunakan untuk nslookup
        self.cliNslookup =  ['nslookup', str(self.tujuan)]

        ## jalankan route ##
        self.p = subprocess.Popen(self.cliNslookup, stdout=subprocess.PIPE)

        # extract output dari subprocess
        (output, err) = self.p.communicate()

        respon = output
        self.emit(QtCore.SIGNAL("updateResponNslookupTextEdit(QString)"), respon)

        # beritahukan bahwa traceroute telah selesai
        self.print_exit()

    # method untuk menampilkan data ke GUI saat traceroute sudah dimulai
    def print_start(self):
        # beritahukan bahwa proses traceroute akan dimulai
        respon = "Nslookup sedang diproses ...."
        self.emit(QtCore.SIGNAL("updateInfoResponNslookupLabel(QString)"), respon)


        respon = "\nPYTHON-NSLOOKUP %s " % (self.tujuan)
        self.emit(QtCore.SIGNAL("updateResponNslookupTextEdit(QString)"), respon)

        self.emit(QtCore.SIGNAL("updateResponNslookupTextEdit(QString)"), "----------------------------------------------------------------")

    # method untuk menampilkan data ke GUI saat traceroute sudah selesai
    def print_exit(self):
        respon = "Nslookup selesai dijalankan"
        self.emit(QtCore.SIGNAL("updateInfoResponNslookupLabel(QString)"), respon)

         # cetak output di form
        respon = "\n----%s PYTHON NSLOOKUP selesai dijalankan ----" % (self.tujuan)
        self.emit(QtCore.SIGNAL("updateResponNslookupTextEdit(QString)"), respon)
