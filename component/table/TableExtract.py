from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt


class TableExtract(QTableWidget):
    def __init__(self, columns, df):
        QTableWidget.__init__(self)
        self.columns, self.df = columns, df
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
                item = QTableWidgetItem(format(int(data), ','))
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                item.setFlags(Qt.ItemIsEditable)
                self.setItem(row, col, item)
        self.verticalHeader().setVisible(False)
        self.resizeColumnsToContents()
