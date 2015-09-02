# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'led_dialog.ui'
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

class Ui_Dialog_led(object):
    def setupUi(self, Dialog_led):
        Dialog_led.setObjectName(_fromUtf8("Dialog_led"))
        Dialog_led.resize(480, 252)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog_led)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.stackedWidget = QtGui.QStackedWidget(Dialog_led)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.page)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.pushButton_next1 = QtGui.QPushButton(self.page)
        self.pushButton_next1.setObjectName(_fromUtf8("pushButton_next1"))
        self.verticalLayout_2.addWidget(self.pushButton_next1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(self.page_2)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.pushButton_next2 = QtGui.QPushButton(self.page_2)
        self.pushButton_next2.setObjectName(_fromUtf8("pushButton_next2"))
        self.verticalLayout_3.addWidget(self.pushButton_next2)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_3 = QtGui.QLabel(self.page_3)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.pushButton_next3 = QtGui.QPushButton(self.page_3)
        self.pushButton_next3.setObjectName(_fromUtf8("pushButton_next3"))
        self.verticalLayout_4.addWidget(self.pushButton_next3)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(Dialog_led)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog_led)

    def retranslateUi(self, Dialog_led):
        Dialog_led.setWindowTitle(_translate("Dialog_led", "Dialog", None))
        self.label.setText(_translate("Dialog_led", "<html><head/><body><p>Ensure that the LED is <span style=\" color:#ff0000;\">RED</span>. Click &quot;next&quot; to continue. </p></body></html>", None))
        self.pushButton_next1.setText(_translate("Dialog_led", "Next", None))
        self.label_2.setText(_translate("Dialog_led", "<html><head/><body><p>Ensure that the LED is <span style=\" color:#00ff00;\">GREEN</span>. Click &quot;next&quot; to continue. </p></body></html>", None))
        self.pushButton_next2.setText(_translate("Dialog_led", "Next", None))
        self.label_3.setText(_translate("Dialog_led", "<html><head/><body><p>Ensure that the LED is <span style=\" color:#0000ff;\">BLUE</span>. Click &quot;Finish&quot; to complete the test. </p></body></html>", None))
        self.pushButton_next3.setText(_translate("Dialog_led", "Finish", None))

