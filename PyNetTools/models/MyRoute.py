#!/usr/bin/python

import subprocess

from PyQt4 import QtCore

class MyRoute(QtCore.QThread):

    # Konstruktor untuk class MyTraceroute
    def __init__(self):
        # buat objek QThread yang merupakan parent dari class ini
        QtCore.QThread.__init__(self)

    # method ini akan dieksekusi saat class ini dijalankankan dalam thread
    def run(self):
        # beritahukan bahwa traceroute akan dimulai
        self.print_start()

        # perintah di linux yang akan digunakan untuk route
        self.cliRoute =  ['route']

        ## jalankan route ##
        self.p = subprocess.Popen(self.cliRoute, stdout=subprocess.PIPE)

        # extract output dari subprocess
        (output, err) = self.p.communicate()

        respon = output
        self.emit(QtCore.SIGNAL("updateResponRouteTextEdit(QString)"), respon)

        # beritahukan bahwa traceroute telah selesai
        self.print_exit()

    # method untuk menampilkan data ke GUI saat traceroute sudah dimulai
    def print_start(self):
        # beritahukan bahwa proses traceroute akan dimulai
        respon = "Route sedang diproses ...."
        self.emit(QtCore.SIGNAL("updateInfoResponRouteLabel(QString)"), respon)


        respon = "\nPYTHON-ROUTE"
        self.emit(QtCore.SIGNAL("updateResponRouteTextEdit(QString)"), respon)

        self.emit(QtCore.SIGNAL("updateResponRouteTextEdit(QString)"), "----------------------------------------------------------------")

    # method untuk menampilkan data ke GUI saat traceroute sudah selesai
    def print_exit(self):
        respon = "Route selesai dijalankan"
        self.emit(QtCore.SIGNAL("updateInfoResponRouteLabel(QString)"), respon)

         # cetak output di form
        respon = "\n---- PYTHON ROUTE selesai dijalankan ----"
        self.emit(QtCore.SIGNAL("updateResponRouteTextEdit(QString)"), respon)
