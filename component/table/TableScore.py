from PyQt5.QtWidgets import *


class TableScore(QTableWidget):
    def __init__(self):
        QTableWidget.__init__(self)
        self.__component__()
        
