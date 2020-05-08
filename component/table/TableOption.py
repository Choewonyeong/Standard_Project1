from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from setting.Connector import connector
from component.materials.CheckBox import CheckBox
from component.materials.Item import Item
from setting.FontColor import PlusColor
from setting.FontColor import MinusColor


class TableOption(QWidget):

    minusPointRow = [3, 4, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]

    def __init__(self):
        QWidget.__init__(self)
        self.connOption = connector[1]
        self.__variables__()
        self.__component__()

    def __variables__(self):
        self.checked = []
        self.columns, self.dfOption = self.connOption.ColumnAndDfOption()
        self.columns = ['선택'] + self.columns

    def __component__(self):
        self.__tblOption__()
        self.__layout__()

    def __checkBox__(self, table, row, col):
        item = Item()
        checkBox = CheckBox(item)
        checkBox.clicked.connect(self.CheckBoxClick)
        table.setItem(row, col, item)
        table.setCellWidget(row, col, checkBox)

    def CheckBoxClick(self, value):
        row = self.tblOption.currentRow()
        if value:
            self.checked.append(row)
        elif not value:
            self.checked.remove(row)

    def __tblOption__(self):
        self.tblOption = QTableWidget()
        self.tblOption.setRowCount(0)
        self.tblOption.setColumnCount(len(self.columns))
        self.tblOption.setHorizontalHeaderLabels(self.columns)
        for row, lst in enumerate(self.dfOption.values):
            self.tblOption.insertRow(row)
            self.tblOption.setRowHeight(row, 70)
            self.__checkBox__(self.tblOption, row, 0)
            for col, data in enumerate(lst):
                item = QTableWidgetItem(str(data))
                item.setFlags(Qt.ItemIsEditable)
                if col == 3 and row in self.minusPointRow:
                    item.setForeground(MinusColor)
                elif col == 3 and row not in self.minusPointRow:
                    item.setForeground(PlusColor)
                self.tblOption.setItem(row, col+1, item)
        self.tblOption.verticalHeader().setVisible(False)
        self.tblOption.resizeColumnsToContents()
        self.tblOption.setColumnWidth(2, 625)

    def __layout__(self):
        layout = QHBoxLayout()
        layout.addWidget(self.tblOption)
        self.setLayout(layout)




