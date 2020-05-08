from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from setting.Connector import connector
from component.dialog.DialogMessageBox import DialogMessageBox


class DialogSignUp(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.connUser = connector[0]
        self.__setting__()
        self.__component__()

    def __setting__(self):
        self.setWindowFlag(Qt.FramelessWindowHint)

    def __component__(self):
        self.__lineEdit__()
        self.__button__()
        self.__layout__()

    def __lineEdit__(self):
        self.lineEditUserId = QLineEdit()
        self.lineEditUserName = QLineEdit()
        self.lineEditPassword = QLineEdit()
        self.lineEditPassword.setEchoMode(QLineEdit.Password)

    def __button__(self):
        btnClose = QPushButton('취소')
        btnClose.clicked.connect(self.close)
        btnClose.setMouseTracking(False)
        btnApply = QPushButton('가입신청')
        btnApply.clicked.connect(self.btnApplyClick)
        btnApply.setMouseTracking(False)
        btnApply.setDefault(True)
        btnApply.setShortcut('Return')
        self.layoutBtn = QHBoxLayout()
        self.layoutBtn.addWidget(btnClose)
        self.layoutBtn.addWidget(btnApply)

    def btnApplyClick(self):
        userId = self.lineEditUserId.text()
        userName = self.lineEditUserName.text()
        userPassword = self.lineEditPassword.text()
        self.connUser.InsertUserInfo(userId, userName, userPassword)
        dig = DialogMessageBox('가입신청이 등록되었습니다.\n관리자의 승인이 필요합니다.\n관리자:(정)박준현|(부)김재환')
        dig.exec_()
        self.close()

    def __layout__(self):
        layout = QFormLayout()
        layout.addRow('아이디', self.lineEditUserId)
        layout.addRow('성  명', self.lineEditUserName)
        layout.addRow('비밀번호', self.lineEditPassword)
        layout.addItem(self.layoutBtn)
        self.setLayout(layout)