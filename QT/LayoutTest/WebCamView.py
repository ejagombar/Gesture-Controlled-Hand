import sys
import cv2
import mediapipe as mp
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage


class CamThread(QThread):
    updateFrame = Signal(QImage)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.status = True
        self.mp_hands = mp.solutions.hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
        )
        self.mp_drawing = mp.solutions.drawing_utils

    def run(self):
        cap = cv2.VideoCapture(0)

        while self.status:
            ret, frame = cap.read()
            if not ret:
                continue

            color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            HAND_PALM_CONNECTIONS = ((0, 1), (1, 5), (9, 13), (13, 17), (5, 9), (0, 17))
            HAND_THUMB_CONNECTIONS = ((1, 2), (2, 3), (3, 4))
            HAND_INDEX_FINGER_CONNECTIONS = ((5, 6), (6, 7), (7, 8))
            HAND_MIDDLE_FINGER_CONNECTIONS = ((9, 10), (10, 11), (11, 12))
            HAND_RING_FINGER_CONNECTIONS = ((13, 14), (14, 15), (15, 16))
            HAND_PINKY_FINGER_CONNECTIONS = ((17, 18), (18, 19), (19, 20))

            HAND_CONNECTIONS = frozenset().union(
                *[
                    HAND_PALM_CONNECTIONS,
                    HAND_THUMB_CONNECTIONS,
                    HAND_INDEX_FINGER_CONNECTIONS,
                    HAND_MIDDLE_FINGER_CONNECTIONS,
                    HAND_RING_FINGER_CONNECTIONS,
                    HAND_PINKY_FINGER_CONNECTIONS,
                ]
            )

            results = self.mp_hands.process(color_frame)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Modify drawing spec to draw lines in red and make them thicker
                    drawing_spec = self.mp_drawing.DrawingSpec(
                        color=(200, 200, 200), thickness=2, circle_radius=0
                    )
                    self.mp_drawing.draw_landmarks(
                        color_frame,
                        hand_landmarks,
                        HAND_CONNECTIONS,
                        drawing_spec,
                        drawing_spec,
                        False,
                    )

            h, w, ch = color_frame.shape
            img = QImage(color_frame.data, w, h, ch * w, QImage.Format.Format_RGB888)

            self.updateFrame.emit(img)

        cap.release()
        sys.exit(-1)
