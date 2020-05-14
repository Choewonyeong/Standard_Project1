from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class WidgetTables(QWidget):
    def __init__(self, names, objects):
        QWidget.__init__(self)
        self.names = names
        self.objects = objects
        self.__layout__()

    def __layout__(self):
        layout = QHBoxLayout()
        for name, table in zip(self.names, self.objects):
            lblName = QLabel(name)
            lblName.setAlignment(Qt.AlignCenter)
            layoutObject = QVBoxLayout()
            layoutObject.addWidget(lblName)
            layoutObject.addWidget(table, 10)
            layout.addLayout(layoutObject)
        self.setLayout(layout)