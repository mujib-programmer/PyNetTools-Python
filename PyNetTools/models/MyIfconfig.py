#!/usr/bin/python

import subprocess

from PyQt4 import QtCore

class MyIfconfig(QtCore.QThread):

    # Konstruktor untuk class MyTraceroute
    def __init__(self):
        # buat objek QThread yang merupakan parent dari class ini
        QtCore.QThread.__init__(self)

    # method ini akan dieksekusi saat class ini dijalankankan dalam thread
    def run(self):
        # beritahukan bahwa traceroute akan dimulai
        self.print_start()

        # perintah di linux yang akan digunakan untuk ifconfig
        self.cliIfconfig =  ['ifconfig']

        ## jalankan ifconfig ##
        self.p = subprocess.Popen(self.cliIfconfig, stdout=subprocess.PIPE)

        # extract output dari subprocess
        (output, err) = self.p.communicate()

        respon = output
        self.emit(QtCore.SIGNAL("updateResponIfconfigTextEdit(QString)"), respon)

        # beritahukan bahwa traceroute telah selesai
        self.print_exit()

    # method untuk menampilkan data ke GUI saat traceroute sudah dimulai
    def print_start(self):
        # beritahukan bahwa proses traceroute akan dimulai
        respon = "Ifconfig sedang diproses ...."
        self.emit(QtCore.SIGNAL("updateInfoResponIfconfigLabel(QString)"), respon)


        respon = "\nPYTHON-IFCONFIG"
        self.emit(QtCore.SIGNAL("updateResponIfconfigTextEdit(QString)"), respon)

        self.emit(QtCore.SIGNAL("updateResponIfconfigTextEdit(QString)"), "----------------------------------------------------------------")

    # method untuk menampilkan data ke GUI saat traceroute sudah selesai
    def print_exit(self):
        respon = "Ifconfig selesai dijalankan"
        self.emit(QtCore.SIGNAL("updateInfoResponIfconfigLabel(QString)"), respon)

         # cetak output di form
        respon = "\n---- PYTHON IFCONFIG selesai dijalankan ----"
        self.emit(QtCore.SIGNAL("updateResponIfconfigTextEdit(QString)"), respon)
