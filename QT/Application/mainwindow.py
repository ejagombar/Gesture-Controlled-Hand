import sys

from PySide6.QtCore import Qt, Slot, Signal
from PySide6.QtGui import QImage, QPixmap, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QColorDialog
from PySide6.QtSerialPort import QSerialPort
from WebCamView import CamThread
import time

from ui_form import Ui_MainWindow

# Important:
# pyside6-designer form.ui && pyside6-uic form.ui -o ui_form.py


def send_data(serial_port):
    # This function will be called in a loop to send the data
    data = b'test'  # Convert string to bytes
    serial_port.write(data)




class MainWindow(QMainWindow):
    sendSignal = Signal(int, int, int, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.th = CamThread(self)
        self.th.finished.connect(self.close)
        self.th.updateFrame.connect(self.setImage)
        self.th.fingerPositions.connect(self.sendPositionMessage)

        self.serial_port = None
        self.last_executed = 0
        self.sendSignal.connect(self.sendPositionMessage)

        self.ui.IPAddrLineEdit.setText("COM7")

        self.start()


    @Slot(int, int, int, int)
    def sendPositionMessage(self,index,middle,ring,pinky):
        current_time = time.time()
        if current_time - self.last_executed < 0.05:
            return
        self.last_executed = current_time
        if self.serial_port is not None:
            message = f":50,50,{index},100,100,100,[999,999,999,50]"
            self.serial_port.write(message.encode())
            print(message)

    def onConnectButtonClicked(self):
        port_name = self.ui.IPAddrLineEdit.text()
        self.setup_serial_port(port_name)

    def setup_serial_port(self, port_name):
        self.serial_port = QSerialPort()
        self.serial_port.setPortName(port_name)

        if self.serial_port.open(QSerialPort.OpenModeFlag.WriteOnly):
            print(f"Serial port {port_name} opened successfully.")
            self.serial_port.setBaudRate(QSerialPort.BaudRate.Baud115200)
        else:
            print(f"Failed to open serial port {port_name}.")

    def start(self):
        self.th.start()
        self.ui.ColourButton.clicked.connect(self.show_color_picker)

        self.ui.actionOneDark.triggered.connect(self.set_dark_theme)
        self.ui.actionOneLight.triggered.connect(self.set_light_theme)
        self.ui.BrightnessSlider.valueChanged.connect(self.changeBrightness)

        self.ui.ConnectButton.clicked.connect(self.onConnectButtonClicked)

        self.ui.actionOneLight.setChecked(True)  # Default Theme
        self.ui.RainbowRadioButton.setChecked(True)
        self.ui.BrightnessSlider.setValue(25)
        self.ui.actionShow_Webcam_View.setChecked(True)
        self.ui.actionShow_Tracking_Mask.setChecked(True)
        self.ui.actionShow_3D_Visualisation.setEnabled(False)

    def set_dark_theme(self):
        with open("./Themes/OneDark.qss", "r") as f:
            _style = f.read()
            self.setStyleSheet(_style)
        self.ui.actionOneLight.setChecked(False)
        self.ui.actionOneDark.setChecked(True)

    def set_light_theme(self):
        with open("./Themes/OneLight.qss", "r") as f:
            _style = f.read()
            self.setStyleSheet(_style)
        self.ui.actionOneDark.setChecked(False)
        self.ui.actionOneLight.setChecked(True)

    def show_color_picker(self):
        color_dialog = QColorDialog(self)
        color = color_dialog.getColor()
        self.ui.ColourButton.setIcon(self.create_color_icon(color, self.ui.ColourButton.iconSize()))

    def create_color_icon(self, color, size):
        pixmap = QPixmap(size)
        pixmap.fill(color)
        return QIcon(pixmap)

    def changeBrightness(self):
        brightness = self.ui.BrightnessSlider.value()
        self.ui.LEDBrightnessLabel.setText("LED Brightness: " + str(brightness) + "%")

    @Slot(QImage)
    def setImage(self, image):
        scaledImg = image.scaled(self.ui.WebcamTab.width(), self.ui.WebcamTab.height(), Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.WebcamLabel.setPixmap(QPixmap.fromImage(scaledImg))
        self.ui.WebcamLabel.setFixedSize(int(self.ui.WebcamTab.width()*0.98), int(self.ui.WebcamTab.height()*0.98))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("./Themes/OneLight.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
