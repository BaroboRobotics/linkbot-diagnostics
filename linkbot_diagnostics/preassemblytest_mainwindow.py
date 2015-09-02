# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preassemblytest_mainwindow.ui'
#
# Created: Wed Sep  2 16:10:59 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(480, 354)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_led = QtGui.QPushButton(self.centralwidget)
        self.pushButton_led.setObjectName(_fromUtf8("pushButton_led"))
        self.verticalLayout.addWidget(self.pushButton_led)
        self.pushButton_buttons = QtGui.QPushButton(self.centralwidget)
        self.pushButton_buttons.setObjectName(_fromUtf8("pushButton_buttons"))
        self.verticalLayout.addWidget(self.pushButton_buttons)
        self.pushButton_accelerometer = QtGui.QPushButton(self.centralwidget)
        self.pushButton_accelerometer.setObjectName(_fromUtf8("pushButton_accelerometer"))
        self.verticalLayout.addWidget(self.pushButton_accelerometer)
        self.pushButton_encoders = QtGui.QPushButton(self.centralwidget)
        self.pushButton_encoders.setObjectName(_fromUtf8("pushButton_encoders"))
        self.verticalLayout.addWidget(self.pushButton_encoders)
        self.pushButton_motors = QtGui.QPushButton(self.centralwidget)
        self.pushButton_motors.setObjectName(_fromUtf8("pushButton_motors"))
        self.verticalLayout.addWidget(self.pushButton_motors)
        self.pushButton_buzzer = QtGui.QPushButton(self.centralwidget)
        self.pushButton_buzzer.setObjectName(_fromUtf8("pushButton_buzzer"))
        self.verticalLayout.addWidget(self.pushButton_buzzer)
        spacerItem = QtGui.QSpacerItem(20, 88, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_quit = QtGui.QPushButton(self.centralwidget)
        self.pushButton_quit.setObjectName(_fromUtf8("pushButton_quit"))
        self.verticalLayout.addWidget(self.pushButton_quit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_led.setText(_translate("MainWindow", "Test LEDs", None))
        self.pushButton_buttons.setText(_translate("MainWindow", "Test Buttons", None))
        self.pushButton_accelerometer.setText(_translate("MainWindow", "Test Accelerometer", None))
        self.pushButton_encoders.setText(_translate("MainWindow", "Test Encoders", None))
        self.pushButton_motors.setText(_translate("MainWindow", "Test Motors", None))
        self.pushButton_buzzer.setText(_translate("MainWindow", "Beep Buzzer", None))
        self.pushButton_quit.setText(_translate("MainWindow", "Quit", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))

