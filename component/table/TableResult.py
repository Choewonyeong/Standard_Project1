from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from component.materials.CheckBox import CheckBox
from component.materials.Item import Item
from setting import FontColor


class TableResult(QTableWidget):
    def __init__(self, columns, df, Indexes):
        QTableWidget.__init__(self)
        self.columns, self.df = columns, df
        self.columns = ['선택']+self.columns
        self.maxIndex, self.subMaxIndexes = Indexes
        self.checked = []
        self.__component__()

    def __component__(self):
        self.__tableExtract__()

    def __checkBox__(self, row):
        item = Item()
        checkBox = CheckBox(item)
        checkBox.clicked.connect(self.CheckBoxClick)
        self.setItem(row, 0, item)
        self.setCellWidget(row, 0, checkBox)

    def CheckBoxClick(self, value):
        row = self.currentRow()
        if value:
            self.checked.append(row)
        if not value:
            self.checked.remove(row)

    def __tableExtract__(self):
        self.setRowCount(0)
        self.setColumnCount(len(self.columns))
        self.setHorizontalHeaderLabels(self.columns)
        for row, lst in enumerate(self.df.values):
            self.insertRow(row)
            self.__checkBox__(row)
            for col, data in enumerate(lst):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                item.setFlags(Qt.ItemIsEditable)
                if row == self.maxIndex:
                    item.setForeground(FontColor.maxColor)
                elif row in self.subMaxIndexes:
                    item.setForeground(FontColor.subMaxColor)
                self.setItem(row, col+1, item)
        self.verticalHeader().setVisible(False)
        self.resizeColumnsToContents()
        width = 0
        for col in range(self.columnCount()):
            width += self.columnWidth(col)
        self.setFixedWidth(width+20)
