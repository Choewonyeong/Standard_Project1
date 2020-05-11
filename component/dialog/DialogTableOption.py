from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from setting.Connector import connector
from component.materials.CheckBox import CheckBox
from setting.FontColor import PlusColor
from setting.FontColor import MinusColor


class DialogTableOption(QDialog):

    minusPointRow = [3, 4, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]

    def __init__(self):
        QDialog.__init__(self)
        self.connOption = connector[1]
        self.total = 0
        self.__variables__()
        self.__component__()
        self.__setting__()

    def __variables__(self):
        self.checked = []
        self.columns, self.dfOption = self.connOption.ColumnAndDfOption()
        self.columns = ['선택'] + self.columns

    def __component__(self):
        self.__button__()
        self.__tblOption__()
        self.__layout__()

    def __button__(self):
        self.btnClose = QPushButton('닫기')
        self.btnRun = QPushButton('완료')
        self.btnClose.clicked.connect(self.close)
        self.btnRun.clicked.connect(self.BtnRunClick)
        self.layoutBtn = QHBoxLayout()
        self.layoutBtn.addWidget(self.btnClose)
        self.layoutBtn.addWidget(self.btnRun)
        self.layoutBtn.addWidget(QLabel(), 10)

    def BtnRunClick(self):
        try:
            if self.checked:
                for row in self.checked:
                    value = float(self.tblOption.item(row, 4).text())
                    self.total += value
                    self.total = round(self.total, 2)
        except Exception as e:
            print(e)
        self.close()

    def __checkBox__(self, table, row, col):
        checkBox = CheckBox()
        checkBox.clicked.connect(self.CheckBoxClick)
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
            self.tblOption.setRowHeight(row, 50)
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
        self.tblOption.verticalScrollBar().setVisible(False)
        self.tblOption.resizeColumnsToContents()
        self.tblOption.setColumnWidth(2, 625)

    def __layout__(self):
        layout = QVBoxLayout()
        layout.addLayout(self.layoutBtn)
        layout.addWidget(self.tblOption, 10)
        self.setLayout(layout)

    def __setting__(self):
        self.setWindowTitle('신인도 평가 상세 항목')
        width = 45
        for col in range(self.tblOption.columnCount()):
            width += self.tblOption.columnWidth(col)
        self.setFixedWidth(width)
        self.setFixedHeight(800)



