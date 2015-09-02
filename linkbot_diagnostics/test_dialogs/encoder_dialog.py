# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encoder_dialog.ui'
#
# Created: Wed Sep  2 15:23:45 2015
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

class Ui_Dialog_encoder(object):
    def setupUi(self, Dialog_encoder):
        Dialog_encoder.setObjectName(_fromUtf8("Dialog_encoder"))
        Dialog_encoder.resize(332, 343)
        self.gridLayout = QtGui.QGridLayout(Dialog_encoder)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog_encoder)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalSlider_1 = QtGui.QSlider(self.groupBox)
        self.verticalSlider_1.setMaximum(360)
        self.verticalSlider_1.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_1.setObjectName(_fromUtf8("verticalSlider_1"))
        self.verticalLayout_3.addWidget(self.verticalSlider_1)
        self.label_1 = QtGui.QLabel(self.groupBox)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.verticalLayout_3.addWidget(self.label_1)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(Dialog_encoder)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalSlider_2 = QtGui.QSlider(self.groupBox_2)
        self.verticalSlider_2.setMaximum(360)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName(_fromUtf8("verticalSlider_2"))
        self.verticalLayout_2.addWidget(self.verticalSlider_2)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog_encoder)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 3)
        self.groupBox_3 = QtGui.QGroupBox(Dialog_encoder)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalSlider_3 = QtGui.QSlider(self.groupBox_3)
        self.verticalSlider_3.setMaximum(360)
        self.verticalSlider_3.setPageStep(10)
        self.verticalSlider_3.setProperty("value", 0)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName(_fromUtf8("verticalSlider_3"))
        self.verticalLayout.addWidget(self.verticalSlider_3)
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout.addWidget(self.groupBox_3, 1, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(Dialog_encoder)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)

        self.retranslateUi(Dialog_encoder)
        QtCore.QMetaObject.connectSlotsByName(Dialog_encoder)

    def retranslateUi(self, Dialog_encoder):
        Dialog_encoder.setWindowTitle(_translate("Dialog_encoder", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog_encoder", "Encoder 1", None))
        self.label_1.setText(_translate("Dialog_encoder", "0.0", None))
        self.groupBox_2.setTitle(_translate("Dialog_encoder", "Encoder 2", None))
        self.label_2.setText(_translate("Dialog_encoder", "0.0", None))
        self.label_4.setText(_translate("Dialog_encoder", "Move the encoders around with your fingers; check to see that the corresponding sliders also move.", None))
        self.groupBox_3.setTitle(_translate("Dialog_encoder", "Encoder 3", None))
        self.label_3.setText(_translate("Dialog_encoder", "0.0", None))
        self.pushButton.setText(_translate("Dialog_encoder", "Close", None))

