from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from component.method.Score import TranPQScore


class DialogOther(QDialog):
    def __init__(self, widget):
        QDialog.__init__(self)
        self.widget = widget
        self.priceMain = 0
        self.priceSub = 0
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
        self.btnClose.clicked.connect(self.close)
        self.btnAdd = QPushButton('추가')
        self.btnClose.setDefault(True)
        self.btnAdd.clicked.connect(self.BtnAddClick)

    def BtnAddClick(self):
        rowCount = self.tblOther.rowCount()
        self.tblOther.insertRow(rowCount)
        self.__lineEditTitle__(rowCount)
        self.__lineEditPQ__(rowCount)
        self.__lineEditPQTran__(rowCount, False)
        self.__lineEditPoint__(rowCount)
        self.__pushButton__(rowCount)

    def __pushButton__(self, row):
        pushButton = QPushButton('삭제')
        pushButton.clicked.connect(self.PushButtonClick)
        self.tblOther.setCellWidget(row, 4, pushButton)

    def __lineEditTitle__(self, row, boolean=True):
        lineEdit = QLineEdit()
        lineEdit.setEnabled(boolean)
        self.tblOther.setCellWidget(row, 0, lineEdit)

    def __lineEditPQ__(self, row, boolean=True):
        lineEdit = QLineEdit()
        lineEdit.setEnabled(boolean)
        lineEdit.textChanged.connect(self.formatScore)
        self.tblOther.setCellWidget(row, 1, lineEdit)

    def __lineEditPQTran__(self, row, boolean=True):
        lineEdit = QLineEdit()
        lineEdit.setEnabled(boolean)
        self.tblOther.setCellWidget(row, 2, lineEdit)

    def __lineEditPoint__(self, row, boolean=True):
        lineEdit = QLineEdit()
        lineEdit.setEnabled(boolean)
        self.tblOther.setCellWidget(row, 3, lineEdit)

    def PushButtonClick(self):
        row = self.tblOther.currentRow()
        self.tblOther.removeRow(row)

    def __table__(self):
        columns = ['업체명', '기술(PQ)점수', '기술(PQ)점수환산', '신인도점수', '옵션']
        self.tblOther = QTableWidget()
        self.tblOther.setRowCount(0)
        self.tblOther.setColumnCount(len(columns))
        self.tblOther.setHorizontalHeaderLabels(columns)
        self.tblOther.verticalHeader().setVisible(False)
        width = 15
        for col in range(self.tblOther.columnCount()):
            width += self.tblOther.columnWidth(col)
        self.tblOther.setFixedWidth(width)

    def formatScore(self, text):
        col = self.tblOther.currentColumn()
        row = self.tblOther.currentRow()
        self.priceMain = self.widget.priceMain
        self.priceSub = self.widget.priceSub
        if col == 1:
            try:
                lineEditPQTran = self.tblOther.cellWidget(row, 2)
                score = round(float(text), 3)
                scoreTran = TranPQScore(self.priceMain, self.priceSub, score)
                lineEditPQTran.setText(str(scoreTran.__format__('.3f')))
            except:
                pass

    def __layout__(self):
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(self.btnClose)
        layoutBtn.addWidget(self.btnAdd)
        layoutBtn.addWidget(QLabel(), 10)
        layout = QVBoxLayout()
        layout.addLayout(layoutBtn)
        layout.addWidget(self.tblOther, 10)
        self.setLayout(layout)
