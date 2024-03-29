import sys

from PySide6.QtCore import Qt, Slot, Signal
from PySide6.QtGui import QImage, QPixmap, QIcon, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QColorDialog
from PySide6.QtSerialPort import QSerialPort
from PySide6.QtMultimedia import QMediaDevices
from WebCamView import CamThread
import time
import struct
import socket
from storage import * 

from ui_form import Ui_MainWindow

# Important:
# pyside6-designer form.ui && pyside6-uic form.ui -o ui_form.py


# nase evalatiion
class MainWindow(QMainWindow):
    sendSignal = Signal(int, int, int, int)
    selectedCamera = Signal(int)

    def __init__(self, parent=None, config=None):
        super().__init__(parent)
        self.config = config

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.camera_index = None
        self.serial_port = None
        self.udp_conn = None
        self.last_executed = 0
        self.ledColour = [100,100,100]
        self.customColour = [0,0,0]
        self.ledBrightness = 60
        self.setWindowTitle("Gesture Control Client")
        self.sendSignal.connect(self.sendPositionMessage)

        self.start()


    @Slot(int, int, int, int)
    def sendPositionMessage(self,thumbAngle, thumb, index,middle,ring,pinky):
        current_time = time.time()
        if current_time - self.last_executed < 0.005:
            return

        self.last_executed = current_time

        checkSum = thumbAngle + thumb + index + middle + ring + pinky
        buffer = struct.pack('>H', checkSum)

        if self.serial_port is not None:
            message = struct.pack('@11B',thumbAngle,thumb,index,middle,ring,pinky,self.ledColour[0],self.ledColour[1],self.ledColour[2],self.ledBrightness, 1)
            self.serial_port.write(message)

        if self.udp_conn is not None:
            message = struct.pack('@13B',thumbAngle,thumb,index,middle,ring,pinky,self.ledColour[0],self.ledColour[1],self.ledColour[2],self.ledBrightness,buffer[0],buffer[1], 1)
            self.udp_conn.sendall(message)

        self.ui.Progress_Thumb.setValue(thumb)
        self.ui.Progress_ThumbBase.setValue(104-thumbAngle)
        self.ui.Progress_Index.setValue(index)
        self.ui.Progress_Middle.setValue(middle)
        self.ui.Progress_Ring.setValue(ring)
        self.ui.Progress_Pinky.setValue(pinky)

    def sendColourMessage(self):
        message = struct.pack('@11B',0,0,0,0,0,0,self.ledColour[0],self.ledColour[1],self.ledColour[2],self.ledBrightness, 0)
        for _ in range(0,5):
            if self.serial_port is not None:
                self.serial_port.write(message)

            if self.udp_conn is not None:
                self.udp_conn.sendall(message)

        if self.config is not None:
            self.config.ledColour = self.ledColour

    def setup_tcp_connection(self, ip_addr):
        serverAddr = None;
        
        try:
            serverAddr = socket.getaddrinfo(ip_addr.split(":")[0], int(ip_addr.split(":")[1]), socket.AF_INET, socket.SOCK_DGRAM)[0][4]
        except socket.gaierror as e:
            print("Error resolving server address:", e)
            return

        try:
            self.udp_conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.udp_conn.connect(serverAddr)

            self.udp_conn.sendall(b"client1")

        except socket.error as e:
            print("Error connecting to server:", e)

    def onConnectButtonClicked(self):
        port_name = self.ui.IPAddrLineEdit.text()

        if "." in port_name:
            self.setup_tcp_connection(port_name)
        else:
            self.setup_serial_port(port_name)

        self.setStatusTip("Connecting...")
        if self.config is not None:
            self.config.connectionAddr = port_name

    def setup_serial_port(self, port_name):
        self.serial_port = QSerialPort()
        self.serial_port.setPortName(port_name)

        if self.serial_port.open(QSerialPort.OpenModeFlag.WriteOnly):
            self.statusBar().showMessage(f"Serial port {port_name} opened successfully.")
            self.serial_port.setBaudRate(QSerialPort.BaudRate.Baud115200)
            self.ui.ConnectionStatusLabel.setText("Status: Connected")
            self.sendColourMessage()
        else:
            self.statusBar().showMessage(f"Failed to open serial port {port_name}.")

    def start(self):


        self.ui.ColourButton.clicked.connect(self.show_color_picker)

        self.ui.actionOneDark.triggered.connect(self.set_dark_theme)
        self.ui.actionOneLight.triggered.connect(self.set_light_theme)
        self.ui.BrightnessSlider.valueChanged.connect(self.changeBrightness)

        self.ui.ConnectButton.clicked.connect(self.onConnectButtonClicked)
        self.ui.RainbowRadioButton.clicked.connect(self.onRainbowRadioButtonClicked)
        self.ui.CustomRadioButton.clicked.connect(self.onCustomRadioButtonClicked)

        self.status_bar = self.statusBar()

        self.ui.RainbowRadioButton.setChecked(True)
        self.ui.BrightnessSlider.setValue(25)
        self.ui.actionShow_Webcam_View.setChecked(True)
        self.ui.actionShow_Tracking_Mask.setChecked(True)
        self.ui.actionShow_3D_Visualisation.setEnabled(False)

        if self.config is not None:
            self.ledColour = self.config.ledColour
            self.customColour = self.config.customColour
            self.ledBrightness = self.config.ledBrightness
            self.ui.IPAddrLineEdit.setText(self.config.connectionAddr)
            colour = QColor(self.customColour[1], self.customColour[0], self.customColour[2])
            self.ui.ColourButton.setIcon(self.create_color_icon(colour, self.ui.ColourButton.iconSize()))
            self.ui.BrightnessSlider.setValue(self.ledBrightness)
            ledMode = self.config.selectedLEDMode
            if ledMode == 0:
                self.ui.RainbowRadioButton.setChecked(True)
            elif ledMode == 1:
                self.ui.ReactiveRadioButton.setChecked(True)
            else:
                self.ui.CustomRadioButton.setChecked(True)

            if "light" in self.config.colourSchemePath.lower():
                self.ui.actionOneLight.setChecked(True) 
            if "dark" in self.config.colourSchemePath.lower():
                self.ui.actionOneDark.setChecked(True)
                
        self.setupAvailableCameras()



    def setupAvailableCameras(self):
        cameras = QMediaDevices.videoInputs()
        if not cameras:
            self.statusBar().showMessage(f"No cameras found.")
            return
        else:
            for cameraDevice in cameras:
                index = cameras.index(cameraDevice)
                if "ir " not in cameraDevice.description().lower():
                    action = self.ui.menuSelect_Video_Device.addAction(cameraDevice.description())
                    action.triggered.connect(self.make_set_camera_index(index))

                    self.statusBar().showMessage("Opened camera: " + cameraDevice.description())

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
        path = "./Themes/OneDark.qss"
        with open(path, "r") as f:
            _style = f.read()
            self.setStyleSheet(_style)
        self.ui.actionOneLight.setChecked(False)
        self.ui.actionOneDark.setChecked(True)
        if self.config is not None:
            self.config.colourSchemePath = path

    def set_light_theme(self):
        path = "./Themes/OneLight.qss"
        with open(path, "r") as f:
            _style = f.read()
            self.setStyleSheet(_style)
        self.ui.actionOneDark.setChecked(False)
        self.ui.actionOneLight.setChecked(True)
        if self.config is not None:
            self.config.colourSchemePath = path

    def show_color_picker(self):
        color_dialog = QColorDialog(self)
        color = color_dialog.getColor()
        self.ui.ColourButton.setIcon(self.create_color_icon(color, self.ui.ColourButton.iconSize()))
        self.customColour = [color.green(), color.red(), color.blue()]
        if self.ui.CustomRadioButton.isChecked():
            self.ledColour = self.customColour
            self.sendColourMessage()
        if self.config is not None:
            self.config.customColour = self.customColour

    def create_color_icon(self, color, size):
        pixmap = QPixmap(size)
        pixmap.fill(color)
        return QIcon(pixmap)

    def changeBrightness(self):
        brightness = self.ui.BrightnessSlider.value()
        self.ui.LEDBrightnessLabel.setText("LED Brightness: " + str(brightness) + "%")
        self.ledBrightness = int((brightness/100)*255)
        self.sendColourMessage()
        if self.config is not None:
            self.config.ledBrightness = brightness

    def onCustomRadioButtonClicked(self):
        if self.config is not None:
            self.config.selectedLEDMode = 2
        self.ledColour = self.customColour
        self.sendColourMessage()

    def onRainbowRadioButtonClicked(self):
        if self.config is not None:
            self.config.selectedLEDMode = 0
        self.ledColour = [1,1,1]
        print(self.ledColour)
        self.sendColourMessage()

    def onReactiveRadioButtonClicked(self):
        if self.config is not None:
            self.config.selectedLEDMode = 1


    @Slot(QImage)
    def setImage(self, image):
        scaledImg = image.scaled(self.ui.WebcamTab.width(), self.ui.WebcamTab.height(), Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.WebcamLabel.setPixmap(QPixmap.fromImage(scaledImg))
        self.ui.WebcamLabel.setFixedSize(int(self.ui.WebcamTab.width()*0.98), int(self.ui.WebcamTab.height()*0.98))


if __name__ == "__main__":
    app = QApplication(sys.argv)


    config = LoadConfig("config.toml")
    if config == None:
        config = Config()

    with open(config.colourSchemePath) as f:
        _style = f.read()
        app.setStyleSheet(_style)

    widget = MainWindow(None,config)
    widget.show()
    ret = app.exec()
    SaveConfig("config.toml", config)
    print("Exiting...")
    sys.exit(ret)
