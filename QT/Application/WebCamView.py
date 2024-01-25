import sys
import cv2
import mediapipe as mp
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage
import numpy as np

class CamThread(QThread):
    updateFrame = Signal(QImage)
    fingerPositions = Signal(int,int,int, int, int, int)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.status = True
        self.mp_hands = mp.solutions.hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.8,
            min_tracking_confidence=0.8,
        )
        self.mp_drawing = mp.solutions.drawing_utils

    def calcDistance(self, point1, point2):
        return (point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2 + (point1.z - point2.z) ** 2
    
    def sumSquares(self, point1, point2, point3):
        return point1 ** 2 + point2 ** 2 + point3 ** 2

    def calculate_angle(self, point1, point2, point3):
        A = np.array(point1) - np.array(point2)
        B = np.array(point3) - np.array(point2)

        dot_product = np.dot(A, B)

        norm_A = np.linalg.norm(A)
        norm_B = np.linalg.norm(B)

        cos_angle = dot_product / (norm_A * norm_B)

        angle = np.arccos(cos_angle)
        angle_degrees = np.degrees(angle)

        return angle_degrees

    def mapValue (self, value, min1, max1, min2, max2):
        return (value - min1) * (max2 - min2) / (max1 - min1) + min2

    def run(self):
        cap = cv2.VideoCapture(0)


        while self.status:
            ret, frame = cap.read()
            if not ret:
                continue

            color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            color_frame = cv2.flip(color_frame, 1)

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

                points = results.multi_hand_landmarks[0]
                self.computePoints(points)

            h, w, ch = color_frame.shape
            img = QImage(color_frame.data, w, h, ch * w, QImage.Format.Format_RGB888)

            self.updateFrame.emit(img)

        cap.release()
        sys.exit(-1)

    def computePoints(self, points):
        max = [1,1,0.95,1.0,0.95,0.6]
        min = [0.1,0.1,0.12,0.10,0.12,0.08]
        acrossPalm1 = self.calcDistance(points.landmark[1], points.landmark[17])
        acrossPalm2 = self.calcDistance(points.landmark[0], points.landmark[5])
        palmSize = (acrossPalm1 + acrossPalm2) / 2

        indexdistance = self.calcDistance(points.landmark[8], points.landmark[5])
        middledistance = self.calcDistance(points.landmark[12], points.landmark[9])
        ringdistance = self.calcDistance(points.landmark[16], points.landmark[13])
        pinkydistance = self.calcDistance(points.landmark[20], points.landmark[17])
        thumbdistance = self.calcDistance(points.landmark[4], points.landmark[2])
        thumbbasedistance = self.calcDistance(points.landmark[17], points.landmark[2])
        
        thumbBasePos = self.mapValue(thumbbasedistance/palmSize, min[0], max[0], 12, 104)
        thumbPos = self.mapValue(thumbdistance/palmSize, min[1], max[1], 0, 180)
        indexPos = self.mapValue(indexdistance/palmSize, min[2], max[2], 180, 0)
        middlePos = self.mapValue(middledistance/palmSize, min[3], max[3], 180, 0)
        ringPos = self.mapValue(ringdistance/palmSize, min[4], max[4], 180, 0)
        pinkyPos = self.mapValue(pinkydistance/palmSize, min[5], max[5], 180, 0)

        tip = np.array([points.landmark[8].x, points.landmark[8].y, points.landmark[8].z])
        mcp = np.array([points.landmark[5].x, points.landmark[5].y, points.landmark[5].z])

        distance = np.linalg.norm(tip - mcp) * 400
        # calculatedVal = 180 - ((distance + indexPos)/2) * 2

        # angle = self.calculate_angle(points.landmark[0], points.landmark[5], points.landmark[6])
        point1 = [points.landmark[4].x, points.landmark[4].y, points.landmark[4].z]
        point2 = [points.landmark[1].x, points.landmark[1].y, points.landmark[1].z]
        point3 = [points.landmark[0].x, points.landmark[0].y, points.landmark[0].z]
        angle = self.calculate_angle(point1, point2, point3)

        # thumbAngle = self.mapValue(angle, 120, 180, 0, 100)

        # sum = self.sumSquares(indexPos, distance, angle)
        # print(pinkydistance/palmSize)

        self.fingerPositions.emit(thumbBasePos, thumbPos, indexPos, middlePos, ringPos, pinkyPos)

