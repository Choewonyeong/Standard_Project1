from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class DialogOtherManagement(QDialog):
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
        self.btnClose.clicked.connect(self.close)
        self.btnApply = QPushButton('적용')
        self.btnApply.clicked.connect(self.BtnApplyClick)
        self.btnAdd = QPushButton('추가')
        self.btnAdd.clicked.connect(self.BtnAddClick)

    def BtnCloseClick(self):
        for row in range(self.tblOther.rowCount()-1, -1, -1):
            name = self.tblOther.cellWidget(row, 0).text()
            if name == '':
                self.tblOther.removeRow(row)
        self.close()

    def BtnApplyClick(self):
        self.otherInfo.clear()
        for row in range(self.tblOther.rowCount()-1, -1, -1):
            name = self.tblOther.cellWidget(row, 0).text()
            if name == '':
                self.tblOther.removeRow(row)
        for row in range(self.tblOther.rowCount()):
            info = []
            for col in range(self.tblOther.columnCount()-1):
                info.append(self.tblOther.cellWidget(row, col).text())
            self.otherInfo.append(info)

    def BtnAddClick(self):
        rowCount = self.tblOther.rowCount()
        self.tblOther.insertRow(rowCount)
        self.__lineEditTitle__(rowCount)
        self.__lineEditRateStd__(rowCount)
        self.__lineEditCapital__(rowCount)
        self.__lineEditAsset__(rowCount)
        self.__lineEditFlowAsset__(rowCount)
        self.__lineEditFlowFan__(rowCount)
        self.__lineEditPoint__(rowCount)
        self.__pushButton__(rowCount)

    def __lineEditTitle__(self, row, boolean=True):
        lineEdit = QLineEdit()
        lineEdit.setEnabled(boolean)
        self.tblOther.setCellWidget(row, 0, lineEdit)

    def __lineEditRateStd__(self, row, boolean=True):
        lineEdit = QLineEdit()
        lineEdit.setEnabled(boolean)
        self.tblOther.setCellWidget(row, 1, lineEdit)

    def __lineEditCapital__(self, row, boolean=True):
        lineEdit = QLineEdit()
        lineEdit.setEnabled(boolean)
        self.tblOther.setCellWidget(row, 2, lineEdit)

    def __lineEditAsset__(self, row, boolean=True):
        lineEdit = QLineEdit()
        lineEdit.setEnabled(boolean)
        self.tblOther.setCellWidget(row, 3, lineEdit)

    def __lineEditFlowAsset__(self, row, boolean=True):
        lineEdit = QLineEdit()
        lineEdit.setEnabled(boolean)
        self.tblOther.setCellWidget(row, 4, lineEdit)

    def __lineEditFlowFan__(self, row, boolean=True):
        lineEdit = QLineEdit()
        lineEdit.setEnabled(boolean)
        self.tblOther.setCellWidget(row, 5, lineEdit)

    def __lineEditPoint__(self, row, boolean=True):
        lineEdit = QLineEdit()
        lineEdit.setEnabled(boolean)
        self.tblOther.setCellWidget(row, 6, lineEdit)

    def __pushButton__(self, row):
        pushButton = QPushButton('삭제')
        pushButton.clicked.connect(self.PushButtonClick)
        self.tblOther.setCellWidget(row, 7, pushButton)

    def PushButtonClick(self):
        row = self.tblOther.currentRow()
        self.tblOther.removeRow(row)

    def __table__(self):
        columns = ['업체명', '기준비율',
                   '최근년도\n자기자본', '최근년도\n총자산',
                   '최근년도\n유동자산', '최근년도\n유동부채',
                   '신인도점수', '옵션']
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
        layoutBtn.addWidget(self.btnApply)
        layoutBtn.addWidget(self.btnAdd)
        layoutBtn.addWidget(QLabel(), 10)
        layout = QVBoxLayout()
        layout.addLayout(layoutBtn)
        layout.addWidget(self.tblOther, 10)
        self.setLayout(layout)
