from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from setting import Path


class Loading(QSplashScreen):
    def __init__(self):
        QSplashScreen.__init__(self)
        self.setPixmap(QPixmap(Path.imgLogo).scaledToWidth(500))
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.mousePressEvent = self.MousePressEvent
        self.keyPressEvent = self.KeyPressEvent

    def MousePressEvent(self, e):
        pass

    def KeyPressEvent(self, e):
        pass
