# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'motor_dialog.ui'
#
# Created: Wed Sep  2 15:41:48 2015
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

class Ui_Dialog_motor(object):
    def setupUi(self, Dialog_motor):
        Dialog_motor.setObjectName(_fromUtf8("Dialog_motor"))
        Dialog_motor.resize(465, 273)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog_motor)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_positive = QtGui.QPushButton(Dialog_motor)
        self.pushButton_positive.setObjectName(_fromUtf8("pushButton_positive"))
        self.verticalLayout.addWidget(self.pushButton_positive)
        self.pushButton_stop = QtGui.QPushButton(Dialog_motor)
        self.pushButton_stop.setObjectName(_fromUtf8("pushButton_stop"))
        self.verticalLayout.addWidget(self.pushButton_stop)
        self.pushButton_negative = QtGui.QPushButton(Dialog_motor)
        self.pushButton_negative.setObjectName(_fromUtf8("pushButton_negative"))
        self.verticalLayout.addWidget(self.pushButton_negative)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_close = QtGui.QPushButton(Dialog_motor)
        self.pushButton_close.setObjectName(_fromUtf8("pushButton_close"))
        self.verticalLayout.addWidget(self.pushButton_close)

        self.retranslateUi(Dialog_motor)
        QtCore.QMetaObject.connectSlotsByName(Dialog_motor)

    def retranslateUi(self, Dialog_motor):
        Dialog_motor.setWindowTitle(_translate("Dialog_motor", "Dialog", None))
        self.pushButton_positive.setText(_translate("Dialog_motor", "Rotate Counterclockwise", None))
        self.pushButton_stop.setText(_translate("Dialog_motor", "Stop", None))
        self.pushButton_negative.setText(_translate("Dialog_motor", "Rotate Clockwise", None))
        self.pushButton_close.setText(_translate("Dialog_motor", "Close", None))

