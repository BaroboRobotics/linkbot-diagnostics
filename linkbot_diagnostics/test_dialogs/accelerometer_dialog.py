# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accelerometer_dialog.ui'
#
# Created: Wed Sep  2 15:41:47 2015
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

class Ui_Dialog_accelerometer(object):
    def setupUi(self, Dialog_accelerometer):
        Dialog_accelerometer.setObjectName(_fromUtf8("Dialog_accelerometer"))
        Dialog_accelerometer.resize(332, 343)
        self.gridLayout = QtGui.QGridLayout(Dialog_accelerometer)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog_accelerometer)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalSlider_1 = QtGui.QSlider(self.groupBox)
        self.verticalSlider_1.setMaximum(200)
        self.verticalSlider_1.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_1.setObjectName(_fromUtf8("verticalSlider_1"))
        self.verticalLayout_3.addWidget(self.verticalSlider_1)
        self.label_1 = QtGui.QLabel(self.groupBox)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.verticalLayout_3.addWidget(self.label_1)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(Dialog_accelerometer)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalSlider_2 = QtGui.QSlider(self.groupBox_2)
        self.verticalSlider_2.setMaximum(200)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName(_fromUtf8("verticalSlider_2"))
        self.verticalLayout_2.addWidget(self.verticalSlider_2)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog_accelerometer)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 3)
        self.groupBox_3 = QtGui.QGroupBox(Dialog_accelerometer)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalSlider_3 = QtGui.QSlider(self.groupBox_3)
        self.verticalSlider_3.setMaximum(200)
        self.verticalSlider_3.setPageStep(10)
        self.verticalSlider_3.setProperty("value", 0)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName(_fromUtf8("verticalSlider_3"))
        self.verticalLayout.addWidget(self.verticalSlider_3)
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout.addWidget(self.groupBox_3, 1, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(Dialog_accelerometer)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)

        self.retranslateUi(Dialog_accelerometer)
        QtCore.QMetaObject.connectSlotsByName(Dialog_accelerometer)

    def retranslateUi(self, Dialog_accelerometer):
        Dialog_accelerometer.setWindowTitle(_translate("Dialog_accelerometer", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog_accelerometer", "X", None))
        self.label_1.setText(_translate("Dialog_accelerometer", "0.0", None))
        self.groupBox_2.setTitle(_translate("Dialog_accelerometer", "Y", None))
        self.label_2.setText(_translate("Dialog_accelerometer", "0.0", None))
        self.label_4.setText(_translate("Dialog_accelerometer", "Tilt the assembly around to make sure all of the accelerometer axes work.", None))
        self.groupBox_3.setTitle(_translate("Dialog_accelerometer", "Z", None))
        self.label_3.setText(_translate("Dialog_accelerometer", "0.0", None))
        self.pushButton.setText(_translate("Dialog_accelerometer", "Close", None))

