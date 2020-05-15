from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class TableScore(QTableWidget):
    def __init__(self, df, scoreType):
        QTableWidget.__init__(self)
        self.columns = ['낙찰률', '낙찰가', '가격점수', scoreType, '신인도점수', '총점']
        self.df = df
        self.__component__()

    def __component__(self):
        self.setRowCount(0)
        self.setColumnCount(len(self.columns))
        self.setHorizontalHeaderLabels(self.columns)
        for row, lst in enumerate(self.df.values):
            self.insertRow(row)
            for col, data in enumerate(lst):
                item = QTableWidgetItem(str(data))
                item.setFlags(Qt.ItemIsEditable)
                self.setItem(row, col, item)
        self.verticalHeader().setVisible(False)
        self.resizeColumnsToContents()
        width = 20
        for col in range(self.columnCount()):
            width += self.columnWidth(col)
        self.setFixedWidth(width)
