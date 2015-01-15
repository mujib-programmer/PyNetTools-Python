# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created: Wed Nov 12 09:36:30 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!


import sys, threading, subprocess

from PyQt4 import QtCore, QtGui
from models.MyPing import *
from models.MyTraceroute import *
from models.MyNslookup import *
from models.MyIfconfig import *
from models.MyRoute import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainForm(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

        # hubungkan dengan signal di objek MyPing
        self.myPing = MyPing()
        self.connect(self.myPing, QtCore.SIGNAL("updateResponPingTextEdit(QString)"),self.updateResponPingTextEdit)
        self.connect(self.myPing, QtCore.SIGNAL("updateInfoResponPingLabel(QString)"), self.updateInfoResponPingLabel)

        # hubungkan dengan signal di objek MyTraceroute
        self.myTraceroute = MyTraceroute()
        self.connect(self.myTraceroute, QtCore.SIGNAL("updateResponTracerouteTextEdit(QString)"),self.updateResponTracerouteTextEdit)
        self.connect(self.myTraceroute, QtCore.SIGNAL("updateInfoResponTracerouteLabel(QString)"), self.updateInfoResponTracerouteLabel)

        # hubungkan dengan signal di objek MyNslookup
        self.myNslookup = MyNslookup()
        self.connect(self.myNslookup, QtCore.SIGNAL("updateResponNslookupTextEdit(QString)"),self.updateResponNslookupTextEdit)
        self.connect(self.myNslookup, QtCore.SIGNAL("updateInfoResponNslookupLabel(QString)"), self.updateInfoResponNslookupLabel)

        # hubungkan dengan signal di objek MyIfconfig
        self.myIfconfig = MyIfconfig()
        self.connect(self.myIfconfig, QtCore.SIGNAL("updateResponIfconfigTextEdit(QString)"),self.updateResponIfconfigTextEdit)
        self.connect(self.myIfconfig, QtCore.SIGNAL("updateInfoResponIfconfigLabel(QString)"), self.updateInfoResponIfconfigLabel)

        # hubungkan dengan signal di objek MyRoute
        self.myRoute = MyRoute()
        self.connect(self.myRoute, QtCore.SIGNAL("updateResponRouteTextEdit(QString)"),self.updateResponRouteTextEdit)
        self.connect(self.myRoute, QtCore.SIGNAL("updateInfoResponRouteLabel(QString)"), self.updateInfoResponRouteLabel)

    # setup komponen-komponen graphical user interface (GUI)
    def setupUi(self, mainForm):
        mainForm.setObjectName(_fromUtf8("mainForm"))
        mainForm.resize(475, 465)
        self.mainTabWidget = QtGui.QTabWidget(mainForm)
        self.mainTabWidget.setGeometry(QtCore.QRect(10, 10, 451, 441))
        self.mainTabWidget.setObjectName(_fromUtf8("mainTabWidget"))
        self.pingTab = QtGui.QWidget()
        self.pingTab.setObjectName(_fromUtf8("pingTab"))
        self.tujuanPingLabel = QtGui.QLabel(self.pingTab)
        self.tujuanPingLabel.setGeometry(QtCore.QRect(20, 30, 66, 17))
        self.tujuanPingLabel.setObjectName(_fromUtf8("tujuanPingLabel"))
        self.tujuanPingLineEdit = QtGui.QLineEdit(self.pingTab)
        self.tujuanPingLineEdit.setGeometry(QtCore.QRect(120, 30, 301, 27))
        self.tujuanPingLineEdit.setObjectName(_fromUtf8("tujuanPingLineEdit"))
        self.infoTujuanPingLabel = QtGui.QLabel(self.pingTab)
        self.infoTujuanPingLabel.setGeometry(QtCore.QRect(120, 60, 301, 20))
        self.infoTujuanPingLabel.setObjectName(_fromUtf8("infoTujuanPingLabel"))
        self.jumlahPingLabel = QtGui.QLabel(self.pingTab)
        self.jumlahPingLabel.setGeometry(QtCore.QRect(20, 90, 101, 17))
        self.jumlahPingLabel.setObjectName(_fromUtf8("jumlahPingLabel"))
        self.jumlahPingSpinBox = QtGui.QSpinBox(self.pingTab)
        self.jumlahPingSpinBox.setGeometry(QtCore.QRect(120, 90, 71, 27))
        self.jumlahPingSpinBox.setMinimum(1)
        self.jumlahPingSpinBox.setMaximum(10)
        self.jumlahPingSpinBox.setObjectName(_fromUtf8("jumlahPingSpinBox"))
        self.jumlahPingTanpaBatasCheckBox = QtGui.QCheckBox(self.pingTab)
        self.jumlahPingTanpaBatasCheckBox.setGeometry(QtCore.QRect(210, 90, 171, 22))
        self.jumlahPingTanpaBatasCheckBox.setObjectName(_fromUtf8("jumlahPingTanpaBatasCheckBox"))
        self.pingPushButton = QtGui.QPushButton(self.pingTab)
        self.pingPushButton.setGeometry(QtCore.QRect(120, 130, 71, 27))
        self.pingPushButton.setObjectName(_fromUtf8("pingPushButton"))
        self.infoResponPingLabel = QtGui.QLabel(self.pingTab)
        self.infoResponPingLabel.setGeometry(QtCore.QRect(20, 170, 411, 17))
        self.infoResponPingLabel.setObjectName(_fromUtf8("infoResponPingLabel"))
        self.stopPingPushButton = QtGui.QPushButton(self.pingTab)
        self.stopPingPushButton.setGeometry(QtCore.QRect(210, 130, 71, 27))
        self.stopPingPushButton.setObjectName(_fromUtf8("stopPingPushButton"))
        self.responPingTextEdit = QtGui.QTextEdit(self.pingTab)
        self.responPingTextEdit.setGeometry(QtCore.QRect(20, 200, 411, 191))
        self.responPingTextEdit.setObjectName(_fromUtf8("responPingTextEdit"))
        self.mainTabWidget.addTab(self.pingTab, _fromUtf8(""))
        self.tracerouteTab = QtGui.QWidget()
        self.tracerouteTab.setObjectName(_fromUtf8("tracerouteTab"))
        self.tujuanTracerouteLabel = QtGui.QLabel(self.tracerouteTab)
        self.tujuanTracerouteLabel.setGeometry(QtCore.QRect(20, 30, 66, 17))
        self.tujuanTracerouteLabel.setObjectName(_fromUtf8("tujuanTracerouteLabel"))
        self.tujuanTracerouteLineEdit = QtGui.QLineEdit(self.tracerouteTab)
        self.tujuanTracerouteLineEdit.setGeometry(QtCore.QRect(120, 30, 301, 27))
        self.tujuanTracerouteLineEdit.setObjectName(_fromUtf8("tujuanTracerouteLineEdit"))
        self.infoTujuanTracerouteLabel = QtGui.QLabel(self.tracerouteTab)
        self.infoTujuanTracerouteLabel.setGeometry(QtCore.QRect(120, 60, 301, 17))
        self.infoTujuanTracerouteLabel.setObjectName(_fromUtf8("infoTujuanTracerouteLabel"))
        self.tracePushButton = QtGui.QPushButton(self.tracerouteTab)
        self.tracePushButton.setGeometry(QtCore.QRect(120, 90, 98, 27))
        self.tracePushButton.setObjectName(_fromUtf8("tracePushButton"))
        self.infoResponTracerouteLabel = QtGui.QLabel(self.tracerouteTab)
        self.infoResponTracerouteLabel.setGeometry(QtCore.QRect(20, 130, 411, 17))
        self.infoResponTracerouteLabel.setObjectName(_fromUtf8("infoResponTracerouteLabel"))
        self.responTracerouteTextEdit = QtGui.QTextEdit(self.tracerouteTab)
        self.responTracerouteTextEdit.setGeometry(QtCore.QRect(20, 160, 411, 231))
        self.responTracerouteTextEdit.setObjectName(_fromUtf8("responTracerouteTextEdit"))
        self.mainTabWidget.addTab(self.tracerouteTab, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tujuanNslookupLabel = QtGui.QLabel(self.tab)
        self.tujuanNslookupLabel.setGeometry(QtCore.QRect(20, 30, 66, 17))
        self.tujuanNslookupLabel.setObjectName(_fromUtf8("tujuanNslookupLabel"))
        self.tujuanNslookupLineEdit = QtGui.QLineEdit(self.tab)
        self.tujuanNslookupLineEdit.setGeometry(QtCore.QRect(120, 30, 301, 27))
        self.tujuanNslookupLineEdit.setObjectName(_fromUtf8("tujuanNslookupLineEdit"))
        self.infoTujuanNslookupLabel = QtGui.QLabel(self.tab)
        self.infoTujuanNslookupLabel.setGeometry(QtCore.QRect(120, 60, 301, 17))
        self.infoTujuanNslookupLabel.setObjectName(_fromUtf8("infoTujuanNslookupLabel"))
        self.responNslookupTextEdit = QtGui.QTextEdit(self.tab)
        self.responNslookupTextEdit.setGeometry(QtCore.QRect(20, 160, 411, 231))
        self.responNslookupTextEdit.setObjectName(_fromUtf8("responNslookupTextEdit"))
        self.infoResponNslookupLabel = QtGui.QLabel(self.tab)
        self.infoResponNslookupLabel.setGeometry(QtCore.QRect(20, 130, 411, 17))
        self.infoResponNslookupLabel.setObjectName(_fromUtf8("infoResponNslookupLabel"))
        self.lookupPushButton = QtGui.QPushButton(self.tab)
        self.lookupPushButton.setGeometry(QtCore.QRect(120, 90, 98, 27))
        self.lookupPushButton.setObjectName(_fromUtf8("lookupPushButton"))
        self.mainTabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.responIfconfigTextEdit = QtGui.QTextEdit(self.tab_2)
        self.responIfconfigTextEdit.setGeometry(QtCore.QRect(20, 80, 411, 311))
        self.responIfconfigTextEdit.setObjectName(_fromUtf8("responIfconfigTextEdit"))
        self.ifconfigPushButton = QtGui.QPushButton(self.tab_2)
        self.ifconfigPushButton.setGeometry(QtCore.QRect(330, 40, 101, 27))
        self.ifconfigPushButton.setObjectName(_fromUtf8("ifconfigPushButton"))
        self.infoResponIfconfigLabel = QtGui.QLabel(self.tab_2)
        self.infoResponIfconfigLabel.setGeometry(QtCore.QRect(20, 50, 301, 17))
        self.infoResponIfconfigLabel.setObjectName(_fromUtf8("infoResponIfconfigLabel"))
        self.mainTabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.responRouteTextEdit = QtGui.QTextEdit(self.tab_3)
        self.responRouteTextEdit.setGeometry(QtCore.QRect(20, 80, 411, 311))
        self.responRouteTextEdit.setObjectName(_fromUtf8("responRouteTextEdit"))
        self.infoResponRouteLabel = QtGui.QLabel(self.tab_3)
        self.infoResponRouteLabel.setGeometry(QtCore.QRect(20, 50, 281, 17))
        self.infoResponRouteLabel.setObjectName(_fromUtf8("infoResponRouteLabel"))
        self.routePushButton = QtGui.QPushButton(self.tab_3)
        self.routePushButton.setGeometry(QtCore.QRect(330, 40, 101, 27))
        self.routePushButton.setObjectName(_fromUtf8("routePushButton"))
        self.mainTabWidget.addTab(self.tab_3, _fromUtf8(""))

        self.retranslateUi(mainForm)
        self.mainTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        mainForm.setWindowTitle(_translate("mainForm", "Python Network Tools", None))
        self.tujuanPingLabel.setText(_translate("mainForm", "Tujuan", None))
        self.tujuanPingLineEdit.setText(_translate("mainForm", "www.detik.com", None))
        self.infoTujuanPingLabel.setText(_translate("mainForm", "( www.domain.com atau 192.168.0.1 )", None))
        self.jumlahPingLabel.setText(_translate("mainForm", "Jumlah Ping", None))
        self.jumlahPingTanpaBatasCheckBox.setText(_translate("mainForm", "tanpa batas", None))
        self.pingPushButton.setText(_translate("mainForm", "Ping", None))
        self.infoResponPingLabel.setText(_translate("mainForm", "info dan status respon", None))
        self.stopPingPushButton.setText(_translate("mainForm", "Stop", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.pingTab), _translate("mainForm", "Ping", None))
        self.tujuanTracerouteLabel.setText(_translate("mainForm", "Tujuan", None))
        self.tujuanTracerouteLineEdit.setText(_translate("mainForm", "www.detik.com", None))
        self.infoTujuanTracerouteLabel.setText(_translate("mainForm", "( www.domain.com atau 192.168.0.1 )", None))
        self.tracePushButton.setText(_translate("mainForm", "Trace", None))
        self.infoResponTracerouteLabel.setText(_translate("mainForm", "info dan status respon", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tracerouteTab), _translate("mainForm", "Traceroute", None))
        self.tujuanNslookupLabel.setText(_translate("mainForm", "Tujuan", None))
        self.tujuanNslookupLineEdit.setText(_translate("mainForm", "www.detik.com", None))
        self.infoTujuanNslookupLabel.setText(_translate("mainForm", "( www.domain.com atau 192.168.0.1 )", None))
        self.infoResponNslookupLabel.setText(_translate("mainForm", "info dan status respon", None))
        self.lookupPushButton.setText(_translate("mainForm", "lookup", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab), _translate("mainForm", "Nslookup", None))
        self.ifconfigPushButton.setText(_translate("mainForm", "Ifconfig", None))
        self.infoResponIfconfigLabel.setText(_translate("mainForm", "Tekan tombol ifconfig untuk memulai!", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab_2), _translate("mainForm", "Ifconfig", None))
        self.infoResponRouteLabel.setText(_translate("mainForm", "Tekan tombol route untuk memulai!", None))
        self.routePushButton.setText(_translate("mainForm", "Route", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab_3), _translate("mainForm", "Route", None))

        ''' hubungkan tombol dengan signal '''
        self.pingPushButton.clicked.connect(self.lakukanPing)
        self.stopPingPushButton.clicked.connect(self.hentikanPing)
        self.tracePushButton.clicked.connect(self.lakukanTrace)
        self.lookupPushButton.clicked.connect(self.lakukanNslookup)
        self.ifconfigPushButton.clicked.connect(self.lakukanIfconfig)
        self.routePushButton.clicked.connect(self.lakukanRoute)

    # method untuk menangani permintaan ping dari GUI
    def lakukanPing(self):
        hostname = str( self.tujuanPingLineEdit.text() )
        timeout = 1000
        packet_size = 55
        unlimited = self.jumlahPingTanpaBatasCheckBox.isChecked()

        # menentukan jumlah ping yang diinginkan
        if unlimited:
            count = None # ping selama tak terbatas / unlimited
        else:
            count = int( self.jumlahPingSpinBox.text() ) # ping sesuai jumlah yang diinputkan di GUI

        # inisialisasi data awal yang diperlukan untuk melakukan ping sesuai keinginan
        self.myPing.initialize(hostname, timeout, packet_size, None, count)

        # jalankan proses ping sebagai thread
        self.myPing.start()

    # method untuk menangani klik tombol stop pada form ping
    def hentikanPing(self):
        # berikan informasi bahwa ping telah dihentikan
        self.infoResponPingLabel.setText( "Ping dihentikan" )

        # hentikan thread yang melakukan ping
        self.myPing.terminate()

    # method untuk menangani permintaan traceroute dari GUI
    def lakukanTrace(self):
        tujuan = str(self.tujuanTracerouteLineEdit.text())
        port = int(33434)
        max_hops = int(30)

        # inisialisasi data awal yang diperlukan untuk traceroute
        self.myTraceroute.initialize(tujuan, port, max_hops)

        # jalankan traceroute sebagai thread
        self.myTraceroute.start()

    # method untuk menangani permintaan nslookup
    def lakukanNslookup(self):
        tujuan = str(self.tujuanNslookupLineEdit.text())

        # inisialisasi data awal yang diperlukan untuk traceroute
        self.myNslookup.initialize(tujuan)

        # jalankan traceroute sebagai thread
        self.myNslookup.start()

    # method untuk menangani permintaan ifconfig
    def lakukanIfconfig(self):
        # jalankan ifconfig sebagai thread
        self.myIfconfig.start()

    # method untuk menangani permintaan route
    def lakukanRoute(self):
        # jalankan route sebagai thread
        self.myRoute.start()

    # method yang menangani respon ping dari class MyPing untuk ditampilkan di GUI
    def updateResponPingTextEdit(self, respon):
        self.responPingTextEdit.append( respon )

    # method yang menangani info proses ping
    def updateInfoResponPingLabel(self, respon):
        self.infoResponPingLabel.setText(respon)

    # method yang menangani respon traceroute dari class MyTraceroute untuk ditampilkan di GUI
    def updateResponTracerouteTextEdit(self, respon):
        self.responTracerouteTextEdit.append( respon )

    # method yang menangani info proses traceroute
    def updateInfoResponTracerouteLabel(self, respon):
        self.infoResponTracerouteLabel.setText(respon)

    # method yang menangani respon nslookup dari class NsLookup untuk ditampilkan di GUI
    def updateResponNslookupTextEdit(self, respon):
        self.responNslookupTextEdit.append( respon )

    # method yang menangani info proses nslookup
    def updateInfoResponNslookupLabel(self, respon):
        self.infoResponNslookupLabel.setText(respon)

    # method yang menangani respon ifconfig dari class MyIfconfig untuk ditampilkan di GUI
    def updateResponIfconfigTextEdit(self, respon):
        self.responIfconfigTextEdit.append( respon )

    # method yang menangani info proses ifconfig
    def updateInfoResponIfconfigLabel(self, respon):
        self.infoResponIfconfigLabel.setText(respon)

     # method yang menangani respon route dari class MyRoute untuk ditampilkan di GUI
    def updateResponRouteTextEdit(self, respon):
        self.responRouteTextEdit.append( respon )

    # method yang menangani info proses route
    def updateInfoResponRouteLabel(self, respon):
        self.infoResponRouteLabel.setText(respon)

    def main():
	app = QtGui.QApplication(sys.argv)
    	ex = Ui_mainForm()
    	ex.show()
    	sys.exit(app.exec_())

''' jalankan form '''
if __name__ == '__main__':
	main()
    
