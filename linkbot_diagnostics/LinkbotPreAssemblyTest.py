#!/usr/bin/env python3

import linkbot
try:
    from testlinkbot import TestLinkbot
except:
    from linkbot_diagnostics.testlinkbot import TestLinkbot
        
import time
import sys
from PyQt4 import QtCore, QtGui

try:
    from preassemblytest_mainwindow import Ui_MainWindow
except:
    from linkbot_diagnostics.preassemblytest_mainwindow import Ui_MainWindow

try:
    from test_dialogs.led_dialog import Ui_Dialog_led
except:
    from linkbot_diagnostics.test_dialogs.led_dialog import Ui_Dialog_led

class LedDialog(QtGui.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Dialog_led()
        self.ui.setupUi(self)

        try:
            self.linkbot = linkbot.Linkbot()
            self.linkbot.setLedColor(255, 0, 0)
        except:
            QtGui.QMessageBox.warning(self, "Error",
                "Could not connect to Linkbot. Please make sure the Linkbot is "
                "plugged into the computer with a working Micro-USB cable." )
            raise 

        # Connect buttons
        self.ui.pushButton_next1.clicked.connect(self.next1)
        self.ui.pushButton_next2.clicked.connect(self.next2)
        self.ui.pushButton_next3.clicked.connect(self.next3)

    def next1(self):
        self.linkbot.setLedColor(0, 255, 0)
        self.ui.stackedWidget.setCurrentIndex(1)

    def next2(self):
        self.linkbot.setLedColor(0, 0, 255)
        self.ui.stackedWidget.setCurrentIndex(2)

    def next3(self):
        self.done(0)
    
class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Linkbot Pre-Assembly Diagnostics')

        # Connect buttons
        self.ui.pushButton_led.clicked.connect(self.runLedTest)

    def runLedTest(self):
        # Show the Led Dialog
        try:
            self.ledDialog = LedDialog(self)
        except Exception as e:
            print(e)
            return
        self.ledDialog.exec_()


def main():
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
