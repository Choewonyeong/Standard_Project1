from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from setting import FontColor


class TableResult(QTableWidget):
    def __init__(self, columns, df, Indexes):
        QTableWidget.__init__(self)
        self.columns, self.df = columns, df
        self.maxIndex, self.subMaxIndexes = Indexes
        self.__component__()

    def __component__(self):
        self.__tableExtract__()

    def __tableExtract__(self):
        self.setRowCount(0)
        self.setColumnCount(len(self.columns))
        self.setHorizontalHeaderLabels(self.columns)
        for row, lst in enumerate(self.df.values):
            self.insertRow(row)
            for col, data in enumerate(lst):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                item.setFlags(Qt.ItemIsEditable)
                if row == self.maxIndex:
                    item.setForeground(FontColor.maxColor)
                elif row in self.subMaxIndexes:
                    item.setForeground(FontColor.subMaxColor)
                self.setItem(row, col, item)
        self.verticalHeader().setVisible(False)
        self.resizeColumnsToContents()
        width = 0
        for col in range(self.columnCount()):
            width += self.columnWidth(col)
        self.setFixedWidth(width+20)