import sys
import cv2
import mediapipe as mp
from PySide6.QtCore import Qt, QThread, Signal, Slot
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class Thread(QThread):
    updateFrame = Signal(QImage)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.status = True
        self.mp_hands = mp.solutions.hands.Hands()
        self.mp_drawing = mp.solutions.drawing_utils

    def run(self):
        cap = cv2.VideoCapture(0)

        while self.status:
            ret, frame = cap.read()
            if not ret:
                continue

            # Convert the frame to RGB
            color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the frame with MediaPipe
            results = self.mp_hands.process(color_frame)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mp_drawing.draw_landmarks(
                        color_frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS
                    )

            h, w, ch = color_frame.shape
            img = QImage(
                color_frame.data, w, h, ch * w, QImage.Format.Format_RGB888
            ).scaled(640 * 2, 480 * 2, Qt.AspectRatioMode.KeepAspectRatio)

            self.updateFrame.emit(img)

        cap.release()
        sys.exit(-1)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hand Landmarks Detection")
        self.setGeometry(0, 0, 640 * 2, 480 * 2)

        self.label = QLabel(self)
        self.label.setFixedSize(640 * 2, 480 * 2)

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
    app = QApplication([])
    w = Window()
    w.show()
    sys.exit(app.exec_())

