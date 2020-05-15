from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from component.method.TransferScoreValue import TransferPrice
from component.method.TransferScoreValue import TransferPoint


class DialogOtherPQ(QDialog):
    def __init__(self, widget):
        QDialog.__init__(self)
        self.widget = widget
        self.otherInfo = []
        self.__setting__()
        self.__component__()

    def __setting__(self):
        self.setWindowFlag(Qt.FramelessWindowHint)

    def __component__(self):
        self.__button__()
        self.__table__()
        self.__layout__()

    def __button__(self):
        self.btnClose = QPushButton('닫기')
        self.btnClose.clicked.connect(self.BtnCloseClick)
        self.btnAdd = QPushButton('추가')
        self.btnAdd.clicked.connect(self.BtnAddClick)

    def BtnCloseClick(self):
        self.otherInfo.clear()
        for row in range(self.tblOther.rowCount()-1, -1, -1):
            name = self.tblOther.cellWidget(row, 0).text()
            if name == '':
                self.tblOther.removeRow(row)

        for row in range(self.tblOther.rowCount()):
            info = []
            name = self.tblOther.cellWidget(row, 0).text()
            priceHigh = self.tblOther.cellWidget(row, 1).text()
            priceLow = self.tblOther.cellWidget(row, 2).text()
            PQ = self.tblOther.cellWidget(row, 3).text()
            point = self.tblOther.cellWidget(row, 4).text()
            info.append(name)
            info.append(TransferPrice(priceHigh))
            info.append(TransferPrice(priceLow))
            info.append(TransferPoint(PQ))
            info.append(TransferPoint(point))
            self.otherInfo.append(info)
        self.close()

    def BtnAddClick(self):
        rowCount = self.tblOther.rowCount()
        self.tblOther.insertRow(rowCount)
        self.__lineEditTitle__(rowCount)
        self.__lineEditPriceHigh__(rowCount)
        self.__lineEditPriceLow__(rowCount)
        self.__lineEditPQ__(rowCount)
        self.__lineEditPoint__(rowCount)
        self.__pushButton__(rowCount)

    def __lineEditTitle__(self, row, boolean=True):
        lineEdit = QLineEdit()
        lineEdit.setEnabled(boolean)
        self.tblOther.setCellWidget(row, 0, lineEdit)

    def transferPrice(self):
        lineEdit = self.sender()
        priceText = lineEdit.text().replace(',', '')
        try:
            priceText = format(int(priceText), ',')
            lineEdit.setText(priceText)
        except:
            pass

    def __lineEditPriceHigh__(self, row, boolean=True):
        lineEdit = QLineEdit()
        lineEdit.setEnabled(boolean)
        lineEdit.textEdited.connect(self.transferPrice)
        self.tblOther.setCellWidget(row, 1, lineEdit)

    def __lineEditPriceLow__(self, row, boolean=True):
        lineEdit = QLineEdit()
        lineEdit.setEnabled(boolean)
        lineEdit.textEdited.connect(self.transferPrice)
        self.tblOther.setCellWidget(row, 2, lineEdit)

    def __lineEditPQ__(self, row, boolean=True):
        lineEdit = QLineEdit()
        lineEdit.setEnabled(boolean)
        self.tblOther.setCellWidget(row, 3, lineEdit)

    def __lineEditPoint__(self, row, boolean=True):
        lineEdit = QLineEdit()
        lineEdit.setEnabled(boolean)
        self.tblOther.setCellWidget(row, 4, lineEdit)

    def __pushButton__(self, row):
        pushButton = QPushButton('삭제')
        pushButton.clicked.connect(self.PushButtonClick)
        self.tblOther.setCellWidget(row, 5, pushButton)

    def PushButtonClick(self):
        row = self.tblOther.currentRow()
        self.tblOther.removeRow(row)

    def __table__(self):
        columns = ['업체명', '추첨가(상한)', '추첨가(하한)', '기술(PQ)점수', '신인도점수', '옵션']
        self.tblOther = QTableWidget()
        self.tblOther.setRowCount(0)
        self.tblOther.setColumnCount(len(columns))
        self.tblOther.setHorizontalHeaderLabels(columns)
        self.tblOther.verticalHeader().setVisible(False)
        width = 15
        for col in range(self.tblOther.columnCount()):
            width += self.tblOther.columnWidth(col)
        self.tblOther.setFixedWidth(width)

    def __layout__(self):
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(self.btnClose)
        layoutBtn.addWidget(self.btnAdd)
        layoutBtn.addWidget(QLabel("      업체명이 입력되지 않은 데이터는 저장되지 않습니다."))
        layoutBtn.addWidget(QLabel(), 10)
        layout = QVBoxLayout()
        layout.addLayout(layoutBtn)
        layout.addWidget(self.tblOther, 10)
        self.setLayout(layout)
