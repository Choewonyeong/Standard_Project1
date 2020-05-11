from PyQt5.QtWidgets import *


class WidgetTablePrice(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.__component__()

    def __component__(self):
        self.__lbl__()
        self.__table__()
        self.__layout__()

