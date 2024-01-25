import sys

from PySide6.QtCore import Qt, Slot, Signal
from PySide6.QtGui import QImage, QPixmap, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QColorDialog
from PySide6.QtSerialPort import QSerialPort
from PySide6.QtMultimedia import QMediaDevices
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
    selectedCamera = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.camera_index = None

        self.serial_port = None
        self.last_executed = 0
        self.ledColour = [100,100,100]
        self.ledBrightness = 60
        self.sendSignal.connect(self.sendPositionMessage)

        self.ui.IPAddrLineEdit.setText("COM7")

        self.start()


    @Slot(int, int, int, int)
    def sendPositionMessage(self,thumbAngle, thumb, index,middle,ring,pinky):
        current_time = time.time()
        if current_time - self.last_executed < 0.005:
            return
        self.last_executed = current_time
        if self.serial_port is not None:
            colourString = f"[{self.ledColour[0]},{self.ledColour[1]},{self.ledColour[2]},{self.ledBrightness}]"
            message = f":{thumbAngle},{thumb},{index},{middle},{ring},{pinky},{colourString}"
            self.serial_port.write(message.encode())
            print(message)

    def sendColourMessage(self):
        if self.serial_port is not None:
            colourString = f"[{self.ledColour[0]},{self.ledColour[1]},{self.ledColour[2]},{self.ledBrightness}]"
            message = f":-1,-1,-1,-1,-1,-1,{colourString}"
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
        self.ui.ColourButton.clicked.connect(self.show_color_picker)

        self.ui.actionOneDark.triggered.connect(self.set_dark_theme)
        self.ui.actionOneLight.triggered.connect(self.set_light_theme)
        self.ui.BrightnessSlider.valueChanged.connect(self.changeBrightness)

        self.ui.ConnectButton.clicked.connect(self.onConnectButtonClicked)
        self.ui.RainbowRadioButton.clicked.connect(self.onRainbowRadioButtonClicked)
        self.ui.CustomRadioButton.clicked.connect(self.sendColourMessage)

        self.ui.actionOneLight.setChecked(True)  # Default Theme
        self.ui.RainbowRadioButton.setChecked(True)
        self.ui.BrightnessSlider.setValue(25)
        self.ui.actionShow_Webcam_View.setChecked(True)
        self.ui.actionShow_Tracking_Mask.setChecked(True)
        self.ui.actionShow_3D_Visualisation.setEnabled(False)
        self.setupAvailableCameras()


    def setupAvailableCameras(self):
        cameras = QMediaDevices.videoInputs()
        if not cameras:
            print("No cameras found")
            return
        else:
            for cameraDevice in cameras:
                index = cameras.index(cameraDevice)
                if "ir " not in cameraDevice.description().lower():
                    action = self.ui.menuSelect_Video_Device.addAction(cameraDevice.description())
                    action.triggered.connect(self.make_set_camera_index(index))

        self.th = CamThread(self)
        self.th.finished.connect(self.close)
        self.th.updateFrame.connect(self.setImage)
        self.th.fingerPositions.connect(self.sendPositionMessage)
        self.th.start()

    @Slot()
    def make_set_camera_index(self, index):
        def set_camera_index():
            self.camera_index = index
        return set_camera_index

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
        self.ledColour = [color.green(), color.red(), color.blue()]
        if self.ui.CustomRadioButton.isChecked():
            self.sendColourMessage()

    def create_color_icon(self, color, size):
        pixmap = QPixmap(size)
        pixmap.fill(color)
        return QIcon(pixmap)

    def changeBrightness(self):
        brightness = self.ui.BrightnessSlider.value()
        self.ui.LEDBrightnessLabel.setText("LED Brightness: " + str(brightness) + "%")
        self.ledBrightness = int((brightness/100)*255)
        self.sendColourMessage()

    def onRainbowRadioButtonClicked(self):
        self.ledColour = [999,999,999]
        self.sendColourMessage()

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
