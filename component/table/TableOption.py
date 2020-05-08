from PyQt5.QtWidgets import QWidget


class TableSubOptions(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.__connector__()
        self.__variables__()
        self.__component__()
