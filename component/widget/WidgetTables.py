from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from component.table.TableScore import TableScore


class WidgetTables(QWidget):
    def __init__(self, names, tables):
        QWidget.__init__(self)
        self.names = names
        self.tables = tables
        self.__layout__()

    def __layout__(self):
        layout = QHBoxLayout()
        for name, table in zip(self.names, self.tables):
            lblName = QLabel(name)
            lblName.setAlignment(Qt.AlignCenter)
            layoutObject = QVBoxLayout()
            layoutObject.addWidget(lblName)
            layoutObject.addWidget(table, 10)
            layout.addLayout(layoutObject)
        self.setLayout(layout)