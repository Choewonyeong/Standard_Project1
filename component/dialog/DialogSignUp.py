from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from setting.Connector import connector
from component.dialog.DialogMessageBox import DialogMessageBox
from design import Style


class DialogSignUp(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.connUser = connector[0]
        self.__setting__()
        self.__variables__()
        self.__component__()

    def __setting__(self):
        self.setStyleSheet(Style.Dialog_SignUp)
        self.setWindowFlag(Qt.FramelessWindowHint)

    def __variables__(self):
        self.userIds = self.connUser.ReturnUserIds()

    def __component__(self):
        self.__lineEdit__()
        self.__button__()
        self.__layout__()

    def __lineEdit__(self):
        self.lineEditUserId = QLineEdit()
        self.lineEditUserName = QLineEdit()
        self.lineEditPassword = QLineEdit()
        self.lineEditPassword.setEchoMode(QLineEdit.Password)
        self.lineEditPasswordConfirm = QLineEdit()
        self.lineEditPasswordConfirm.setEchoMode(QLineEdit.Password)
        self.lineEditUserId.setStyleSheet(Style.LineEdit_Text)
        self.lineEditUserName.setStyleSheet(Style.LineEdit_Text)
        self.lineEditPassword.setStyleSheet(Style.LineEdit_Text)
        self.lineEditPasswordConfirm.setStyleSheet(Style.LineEdit_Text)

    def __button__(self):
        btnClose = QPushButton('취소')
        btnClose.setStyleSheet(Style.PushButton_Close)
        btnClose.setCursor(Qt.PointingHandCursor)
        btnClose.clicked.connect(self.close)
        btnClose.setMouseTracking(False)
        btnApply = QPushButton('가입신청')
        btnApply.setStyleSheet(Style.PushButton_Accept)
        btnApply.setCursor(Qt.PointingHandCursor)
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
        userPasswordConfirm = self.lineEditPasswordConfirm.text()
        if userId == "":
            dig = DialogMessageBox('아이디를 입력하세요.')
            dig.exec_()
        elif userId in self.userIds:
            dig = DialogMessageBox('이미 존재하는 아이디입니다.')
            dig.exec_()
        elif userName == '':
            dig = DialogMessageBox('성명을 입력하세요.')
            dig.exec_()
        elif userPassword == '':
            dig = DialogMessageBox('비밀번호를 입력하세요.')
            dig.exec_()
        elif userPassword != userPasswordConfirm:
            dig = DialogMessageBox('비밀번호가 일치하지 않습니다.')
            dig.exec_()
        else:
            self.connUser.InsertUserInfo(userId, userName, userPassword)
            dig = DialogMessageBox('가입신청이 등록되었습니다.\n관리자의 승인이 필요합니다.\n관리자:(정)박준현|(부)김재환')
            dig.exec_()
            self.close()

    def __layout__(self):
        layout = QFormLayout()
        layout.addRow('아이디', self.lineEditUserId)
        layout.addRow('성  명', self.lineEditUserName)
        layout.addRow('비밀번호', self.lineEditPassword)
        layout.addRow('비밀번호 확인', self.lineEditPasswordConfirm)
        layout.addRow('', QLabel())
        layout.addItem(self.layoutBtn)
        self.setLayout(layout)