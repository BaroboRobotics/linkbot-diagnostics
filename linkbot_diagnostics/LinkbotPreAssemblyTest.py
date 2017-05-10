#!/usr/bin/env python3

import linkbot3 as linkbot
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

try:
    from test_dialogs.encoder_dialog import Ui_Dialog_encoder
except:
    from linkbot_diagnostics.test_dialogs.encoder_dialog import Ui_Dialog_encoder

try:
    from test_dialogs.button_dialog import Ui_Dialog_button
except:
    from linkbot_diagnostics.test_dialogs.button_dialog import Ui_Dialog_button

try:
    from test_dialogs.accelerometer_dialog import Ui_Dialog_accelerometer
except:
    from linkbot_diagnostics.test_dialogs.accelerometer_dialog import Ui_Dialog_accelerometer

try:
    from test_dialogs.motor_dialog import Ui_Dialog_motor
except:
    from linkbot_diagnostics.test_dialogs.motor_dialog import Ui_Dialog_motor

class LedDialog(QtGui.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Dialog_led()
        self.ui.setupUi(self)

        try:
            self.linkbot = linkbot.CLinkbot('locl')
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

class ButtonDialog(QtGui.QDialog):
    buttonSignal = QtCore.pyqtSignal(int, int, int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Dialog_button()
        self.ui.setupUi(self)

        try:
            self.linkbot = linkbot.CLinkbot('locl')
        except:
            QtGui.QMessageBox.warning(self, "Error",
                "Could not connect to Linkbot. Please make sure the Linkbot is "
                "plugged into the computer with a working Micro-USB cable." )
            raise 

        self.ui.pushButton.clicked.connect(self.close)

        self.linkbot.enable_button_events(self._buttonEvent)
        self.buttonSignal.connect(self.buttonEvent)

    def buttonEvent(self, button, state, timestamp):
        checkboxes = [ self.ui.checkBox_1,
                       self.ui.checkBox_2,
                       self.ui.checkBox_3, ]
        if state:
            checkboxes[button].setChecked(True)
        else:
            checkboxes[button].setChecked(False)

    def _buttonEvent(self, button, state, timestamp):
        print("Button click detected")
        self.buttonSignal.emit(button, state, timestamp)

    def close(self):
        self.done(0)

class EncoderDialog(QtGui.QDialog):
    encoderSignal = QtCore.pyqtSignal(int, float, int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Dialog_encoder()
        self.ui.setupUi(self)
    
        try:
            self.linkbot = linkbot.CLinkbot('locl')
        except:
            QtGui.QMessageBox.warning(self, "Error",
                "Could not connect to Linkbot. Please make sure the Linkbot is "
                "plugged into the computer with a working Micro-USB cable." )
            raise 

        for slider in ( self.ui.verticalSlider_1,
                        self.ui.verticalSlider_2,
                        self.ui.verticalSlider_3, ):
            slider.setMaximum(360)

        # Connect button
        self.ui.pushButton.clicked.connect(self.close)

        # Connect encoder callbacks
        self.linkbot.enableEncoderEvents(self.encoderEvent)
        self.encoderSignal.connect(self.processEncoderEvent)

    def __del__(self):
        self.linkbot.disableEncoderEvents()

    def encoderEvent(self, n, angle, timestamp):
        self.encoderSignal.emit(n, angle, timestamp)

    def processEncoderEvent(self, n, angle, timestamp):
        def normalizeAngle(theta):
            while theta > 360:
                theta -= 360
            while theta < 0:
                theta += 360
            return theta
        angle_ = angle
        angle = normalizeAngle(angle)
        if n == 0:
            self.ui.verticalSlider_1.setValue(angle)
            self.ui.label_1.setText('{0:.2f}'.format(angle_))
        elif n == 1:
            self.ui.verticalSlider_2.setValue(angle)
            self.ui.label_2.setText('{0:.2f}'.format(angle_))
        elif n == 2:
            self.ui.verticalSlider_3.setValue(angle)
            self.ui.label_3.setText('{0:.2f}'.format(angle_))

    def close(self):
        self.done(0)

class AccelerometerDialog(QtGui.QDialog):
    accelerometerSignal = QtCore.pyqtSignal(float, float, float, int)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Dialog_accelerometer()
        self.ui.setupUi(self)

        try:
            self.linkbot = linkbot.CLinkbot('locl')
        except:
            QtGui.QMessageBox.warning(self, "Error",
                "Could not connect to Linkbot. Please make sure the Linkbot is "
                "plugged into the computer with a working Micro-USB cable." )
            raise 

        for slider in ( self.ui.verticalSlider_1,
                        self.ui.verticalSlider_2,
                        self.ui.verticalSlider_3, ):
            slider.setMaximum(360)

        # Connect button
        self.ui.pushButton.clicked.connect(self.close)

        self.linkbot.enableAccelerometerEvents(self.accelerometerEvent_)
        self.accelerometerSignal.connect(self.accelerometerEvent)

    def __del__(self):
        self.linkbot.disableAccelerometerEvents()

    def accelerometerEvent_(self, x, y, z, timestamp):
        self.accelerometerSignal.emit(x, y, z, timestamp)

    def accelerometerEvent(self, x, y, z, timestamp):
        accels = [x,y,z]
        sliders = [ self.ui.verticalSlider_1,
                    self.ui.verticalSlider_2,
                    self.ui.verticalSlider_3, ]
        labels = [ self.ui.label_1, 
                   self.ui.label_2, 
                   self.ui.label_3, ]
        for a, s, l in zip(accels, sliders, labels):
            s.setValue(a*100)
            l.setText('{0:.2f}'.format(a))

    def close(self):
        self.done(0)

class MotorDialog(QtGui.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Dialog_motor()
        self.ui.setupUi(self)

        # Connect button signals
        self.ui.pushButton_positive.clicked.connect(self.positive)
        self.ui.pushButton_stop.clicked.connect(self.stop)
        self.ui.pushButton_negative.clicked.connect(self.negative)
        self.ui.pushButton_close.clicked.connect(self.close)

        try:
            self.linkbot = linkbot.CLinkbot('locl')
        except:
            QtGui.QMessageBox.warning(self, "Error",
                "Could not connect to Linkbot. Please make sure the Linkbot is "
                "plugged into the computer with a working Micro-USB cable." )
            raise 

    def __del__(self):
        self.linkbot.stop()

    def positive(self):
        self.linkbot.setMotorPowers(128, 128, 128)

    def stop(self):
        self.linkbot.stop()

    def negative(self):
        self.linkbot.setMotorPowers(-128, -128, -128)

    def close(self):
        self.done(0)

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Linkbot Pre-Assembly Diagnostics')

        # Connect buttons
        self.ui.pushButton_led.clicked.connect(self.runLedTest)
        self.ui.pushButton_buttons.clicked.connect(self.runButtonTest)
        self.ui.pushButton_accelerometer.clicked.connect(self.runAccelerometerTest)
        self.ui.pushButton_encoders.clicked.connect(self.runEncoderTest)
        self.ui.pushButton_motors.clicked.connect(self.runMotorTest)
        self.ui.pushButton_buzzer.clicked.connect(self.beep)
        self.ui.pushButton_quit.clicked.connect(self.close)
        self.ui.actionQuit.triggered.connect(self.close)

    def runDialog(self, dialogClass):
        try:
            dialog = dialogClass(self)
        except Exception as e:
            QtGui.QMessageBox.warning(self, "Error",
                "Could not connect to Linkbot: " + str(e) )
            print(e)
            return
        dialog.exec_()

    def runLedTest(self):
        self.runDialog(LedDialog)

    def runButtonTest(self):
        self.runDialog(ButtonDialog)

    def runAccelerometerTest(self):
        self.runDialog(AccelerometerDialog)

    def runEncoderTest(self):
        self.runDialog(EncoderDialog)

    def runMotorTest(self):
        self.runDialog(MotorDialog)

    def beep(self):
        try:
            l = linkbot.CLinkbot('locl')
            l.setBuzzerFrequency(440)
            time.sleep(0.5)
            l.setBuzzerFrequency(0)
        except Exception as e:
            QtGui.QMessageBox.warning(self, "Error",
                "Could not connect to Linkbot: " + str(e) )
            print(e)
            return

    def close(self):
        QtCore.QCoreApplication.instance().quit()

def main():
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
