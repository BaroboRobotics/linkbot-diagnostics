# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'button_dialog.ui'
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

class Ui_Dialog_button(object):
    def setupUi(self, Dialog_button):
        Dialog_button.setObjectName(_fromUtf8("Dialog_button"))
        Dialog_button.resize(444, 184)
        self.gridLayout = QtGui.QGridLayout(Dialog_button)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.checkBox_2 = QtGui.QCheckBox(Dialog_button)
        self.checkBox_2.setCheckable(True)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout.addWidget(self.checkBox_2, 1, 1, 1, 1)
        self.checkBox_1 = QtGui.QCheckBox(Dialog_button)
        self.checkBox_1.setCheckable(True)
        self.checkBox_1.setObjectName(_fromUtf8("checkBox_1"))
        self.gridLayout.addWidget(self.checkBox_1, 1, 0, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(Dialog_button)
        self.checkBox_3.setCheckable(True)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.gridLayout.addWidget(self.checkBox_3, 1, 2, 1, 1)
        self.label = QtGui.QLabel(Dialog_button)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.pushButton = QtGui.QPushButton(Dialog_button)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)

        self.retranslateUi(Dialog_button)
        QtCore.QMetaObject.connectSlotsByName(Dialog_button)

    def retranslateUi(self, Dialog_button):
        Dialog_button.setWindowTitle(_translate("Dialog_button", "Dialog", None))
        self.checkBox_2.setText(_translate("Dialog_button", "Button A", None))
        self.checkBox_1.setText(_translate("Dialog_button", "Button PWR", None))
        self.checkBox_3.setText(_translate("Dialog_button", "Button B", None))
        self.label.setText(_translate("Dialog_button", "Press the Linkbot\'s buttons. Ensure that the corresponding checkmark is checked when each button is depressed.", None))
        self.pushButton.setText(_translate("Dialog_button", "Close", None))

