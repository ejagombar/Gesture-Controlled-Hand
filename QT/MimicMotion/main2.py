import sys
from PySide6.QtGui import QImage
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
)
from PySide6.QtMultimedia import (
    QCamera,
    QImageCapture,
    QMediaCaptureSession,
    QMediaDevices,
)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import QTimer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._capture_session = None
        self._camera = None
        self._camera_info = None
        self._image_capture = None

        available_cameras = QMediaDevices.videoInputs()
        if available_cameras:
            self._camera_info = available_cameras[0]
            self._camera = QCamera(self._camera_info)
            self._image_capture = QImageCapture(self._camera)
            self._capture_session = QMediaCaptureSession(self._camera)
            self._capture_session.setCamera(self._camera)
            self._capture_session.setImageCapture(self._image_capture)

        self._current_preview = QImage()

        self._camera_viewfinder = QVideoWidget()
        self.setCentralWidget(self._camera_viewfinder)

        if (
            self._capture_session
            and self._camera
            and self._camera.error() == QCamera.Error.NoError
        ):
            self._capture_session.setVideoOutput(self._camera_viewfinder)
            self._camera.start()

    def closeEvent(self, event):
        super().closeEvent(event)
        QTimer.singleShot(0, self.stop_camera)

    def stop_camera(self):
        if self._camera and self._camera.isActive():
            self._camera.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    available_geometry = main_win.screen().availableGeometry()
    main_win.resize(
        int(available_geometry.width() / 3), int(available_geometry.height() / 2)
    )
    main_win.show()
    sys.exit(app.exec())

