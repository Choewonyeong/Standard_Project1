from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from setting.Connector import connector


class DialogAdminUser(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.connUser = connector[0]
        self.__variables__()
        self.__component__()
        self.__setting__()

    def __variables__(self):
        self.columns, self.dfUser = self.connUser.ColumnAndDfUser()

    def __component__(self):
        self.__button__()
        self.__table__()
        self.__layout__()

    def __button__(self):
        btnClose = QPushButton('닫기')
        btnClose.clicked.connect(self.close)
        btnSave = QPushButton('엑셀로 저장')
        btnSave.setShortcut('Ctrl+S')
        btnSave.clicked.connect(self.btnSaveClick)
        self.layoutBtn = QHBoxLayout()
        self.layoutBtn.addWidget(btnClose)
        self.layoutBtn.addWidget(btnSave)
        self.layoutBtn.addWidget(QLabel(), 10)

    def btnSaveClick(self):
        pass

    def __table__(self):
        self.tblUser = QTableWidget()
        self.tblUser.setRowCount(0)
        self.tblUser.setColumnCount(len(self.columns))
        self.tblUser.setHorizontalHeaderLabels(self.columns)
        for row, lst in enumerate(self.dfUser.values):
            self.tblUser.insertRow(row)
            self.tblUser.setRowHeight(row, 50)
            for col, data in enumerate(lst):
                item = QTableWidgetItem(data)
                item.setTextAlignment(Qt.AlignCenter)
                if col in [0, 1]:
                    item.setFlags(Qt.ItemIsEditable)
                self.tblUser.setItem(row, col, item)
                self.tblUser.setColumnWidth(col, 100)
        self.tblUser.verticalHeader().setVisible(False)
        self.tblUser.hideColumn(4)

    def __layout__(self):
        layout = QVBoxLayout()
        layout.addLayout(self.layoutBtn)
        layout.addWidget(self.tblUser)
        self.setLayout(layout)

    def __setting__(self):
        width = (len(self.columns)-1)*100+25
        self.setFixedWidth(width)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
