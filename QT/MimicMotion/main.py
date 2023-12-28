import sys
from PySide6.QtCore import Qt, QThread, Signal, Slot, QObject
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
import mediapipe as mp

import cv2


class Thread(QThread):
    updateFrame = Signal(QImage)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.trained_file = None
        self.status = True

    def run(self):
        base_options = mp.tasks.BaseOptions(model_asset_path="./face_landmarker.task")

        options = mp.tasks.vision.FaceLandmarkerOptions(
            base_options=base_options, running_mode=mp.tasks.vision.RunningMode.IMAGE
        )

        cap = cv2.VideoCapture(0)

        while self.status:
            ret, frame = cap.read()
            if not ret:
                continue

            color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            h, w, ch = color_frame.shape
            img = QImage(
                color_frame.data, w, h, ch * w, QImage.Format.Format_RGB888
            ).scaled(640, 480, Qt.AspectRatioMode.KeepAspectRatio)

            self.updateFrame.emit(img)

        cap.release()
        sys.exit(-1)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gesture Control")
        self.setGeometry(0, 0, 640, 480)

        self.label = QLabel(self)
        self.label.setFixedSize(640, 480)

        self.th = Thread(self)
        self.th.finished.connect(self.close)
        self.th.updateFrame.connect(self.setImage)

        self.start()

    def start(self):
        self.th.start()

    @Slot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))


if __name__ == "__main__":
    app = QApplication()
    w = Window()
    w.show()
    sys.exit(app.exec())

