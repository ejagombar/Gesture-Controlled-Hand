import sys

from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow
from WebCamView import CamThread

from ui_form import Ui_MainWindow

# Important:
# pyside6-designer form.ui && pyside6-uic form.ui -o ui_form.py


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.th = CamThread(self)
        self.th.finished.connect(self.close)
        self.th.updateFrame.connect(self.setImage)

        self.start()

    def start(self):
        self.th.start()

    @Slot(QImage)
    def setImage(self, image):
        scaledImg = image.scaled(self.ui.WebcamTab.width(), self.ui.WebcamTab.height(), Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.WebcamLabel.setPixmap(QPixmap.fromImage(scaledImg))
        self.ui.WebcamLabel.setFixedSize(int(self.ui.WebcamTab.width()*0.98), int(self.ui.WebcamTab.height()*0.98))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("OneLight.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
