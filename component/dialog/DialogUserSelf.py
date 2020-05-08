from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from setting.Connector import connector
from component.dialog.DialogMessageBox import DialogMessageBox


class DialogUserSelf(QDialog):
    def __init__(self, userId):
        QDialog.__init__(self)
        self.connUser = connector[0]
        self.userId = userId
        self.__setting__()
        self.__variables__()
        self.__component__()

    def __setting__(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        # setFixedWidth
        # setFixedHeight

    def __variables__(self):
        self.userInfo = self.connUser.ReturnUserInfo(self.userId)

    def __component__(self):
        self.__lineEdit__()
        self.__button__()
        self.__layout__()

    def __lineEdit__(self):
        self.lineEditUserId = QLineEdit()
        self.lineEditUserId.setText(self.userInfo[0])
        self.lineEditUserId.setEnabled(False)
        self.lineEditUserId.setAlignment(Qt.AlignCenter)
        self.lineEditUserName = QLineEdit()
        self.lineEditUserName.setText(self.userInfo[1])
        self.lineEditUserName.setEnabled(False)
        self.lineEditUserName.setAlignment(Qt.AlignCenter)
        self.lineEditPassword = QLineEdit()
        self.lineEditPassword.setEchoMode(QLineEdit.Password)
        self.lineEditPassword.setAlignment(Qt.AlignCenter)
        self.lineEditPasswordConfirm = QLineEdit()
        self.lineEditPasswordConfirm.setEchoMode(QLineEdit.Password)
        self.lineEditPasswordConfirm.setAlignment(Qt.AlignCenter)

    def __button__(self):
        btnClose = QPushButton('닫기')
        btnClose.clicked.connect(self.close)
        btnClose.setMouseTracking(False)
        btnApply = QPushButton('적용')
        btnApply.clicked.connect(self.btnApplyClick)
        btnApply.setMouseTracking(False)
        btnApply.setDefault(True)
        self.layoutBtn = QHBoxLayout()
        self.layoutBtn.addWidget(btnClose)
        self.layoutBtn.addWidget(btnApply)

    def btnApplyClick(self):
        userPassword = self.lineEditPassword.text()
        userPasswordConfirm = self.lineEditPasswordConfirm.text()
        if len(userPassword) < 8:
            dig = DialogMessageBox('비밀번호는 8자리 이상입니다.')
            dig.exec_()
        elif userPassword != userPasswordConfirm:
            dig = DialogMessageBox('비밀번호가 맞지 않습니다.')
            dig.exec_()
        elif userPassword != self.userInfo[2]:
            self.connUser.UpdatePassword(userPassword, self.userId)
            dig = DialogMessageBox('비밀번호가 변경되었습니다.')
            dig.exec_()
            self.close()

    def __layout__(self):
        layout = QFormLayout()
        layout.addRow('아이디', self.lineEditUserId)
        layout.addRow('성  명', self.lineEditUserName)
        layout.addRow('비밀번호 입력', self.lineEditPassword)
        layout.addRow('비밀번호 재입력', self.lineEditPasswordConfirm)
        layout.addItem(self.layoutBtn)
        self.setLayout(layout)
