from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from setting import Path
from setting.Connector import connector
from component.dialog.DialogSignUp import DialogSignUp
from design import Style


class Login(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.connUser = connector[0]
        self.__setting__()
        self.__variables__()
        self.__component__()

    def __setting__(self):
        self.setStyleSheet(Style.Dialog_Login)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedHeight(600)
        self.setFixedWidth(400)

    def __variables__(self):
        self.userIds = self.connUser.ReturnUserIds()

    def __component__(self):
        self.__image__()
        self.__label__()
        self.__input__()
        self.__buttons__()
        self.__layout__()

    def __image__(self):
        self.img = QLabel()
        self.img.setPixmap(QPixmap(Path.imgLogin).scaledToWidth(125))
        self.img.setAlignment(Qt.AlignCenter)
        self.logo = QLabel()
        self.logo.setPixmap(QPixmap(Path.imgLogo).scaledToWidth(200))
        self.logo.setAlignment(Qt.AlignCenter)

    def __label__(self):
        self.cautionUserId = QLabel()
        self.cautionPassword = QLabel()
        self.cautionAccount = QLabel()
        self.cautionUserId.setStyleSheet(Style.Label_Caution)
        self.cautionPassword.setStyleSheet(Style.Label_Caution)
        self.cautionAccount.setStyleSheet(Style.Label_Caution)
        self.cautionUserId.setAlignment(Qt.AlignCenter)
        self.cautionPassword.setAlignment(Qt.AlignCenter)
        self.cautionAccount.setAlignment(Qt.AlignCenter)
        self.cautionUserId.setVisible(False)
        self.cautionPassword.setVisible(False)
        self.cautionAccount.setVisible(False)

    def __input__(self):
        self.inputUserId = QLineEdit()
        self.inputUserId.setMouseTracking(False)
        self.inputUserId.setPlaceholderText('ID')
        self.inputUserId.setAlignment(Qt.AlignCenter)
        self.inputUserId.textChanged.connect(self.checkUserIdNull)
        self.inputPassword = QLineEdit()
        self.inputPassword.setMouseTracking(False)
        self.inputPassword.setPlaceholderText('Password')
        self.inputPassword.setAlignment(Qt.AlignCenter)
        self.inputPassword.setEchoMode(QLineEdit.Password)
        self.inputPassword.textChanged.connect(self.checkPasswordNull)

    def checkUserIdNull(self, text):
        if len(text) != 0:
            self.cautionUserId.setVisible(False)

    def checkPasswordNull(self, text):
        if len(text) != 0:
            self.cautionPassword.setVisible(False)

    def __buttons__(self):
        btnClose = QPushButton()
        btnClose.setText('종료')
        btnClose.setStyleSheet(Style.PushButton_Close)
        btnClose.setCursor(Qt.PointingHandCursor)
        btnClose.clicked.connect(self.btnCloseClick)
        btnLogin = QPushButton()
        btnLogin.setText('로그인')
        btnLogin.setStyleSheet(Style.PushButton_Accept)
        btnLogin.setCursor(Qt.PointingHandCursor)
        btnLogin.clicked.connect(self.btnLoginClick)
        btnLogin.setDefault(True)
        btnLogin.setShortcut('Return')
        self.btnSignup = QPushButton()
        self.btnSignup.setText('회원가입')
        self.btnSignup.setStyleSheet(Style.PushButton_SignUp)
        self.btnSignup.setCursor(Qt.PointingHandCursor)
        self.btnSignup.clicked.connect(self.btnSignupClick)
        self.layoutBtn = QHBoxLayout()
        self.layoutBtn.addWidget(btnClose)
        self.layoutBtn.addWidget(btnLogin)

    def btnCloseClick(self):
        self.userId = ''
        self.close()

    def btnLoginClick(self):
        self.userId = self.inputUserId.text()
        self.password = self.inputPassword.text()
        self.approval = self.connUser.ReturnApproval(self.userId)
        if self.userId == '':
            self.cautionUserId.setText('아이디를 입력하세요.')
            self.cautionUserId.setVisible(True)
        elif self.userId not in self.userIds:
            self.cautionUserId.setText('등록되지 않은 아이디입니다.')
            self.cautionUserId.setVisible(True)
        elif self.password == '':
            self.cautionPassword.setText('비밀번호를 입력하세요.')
            self.cautionPassword.setVisible(True)
        elif self.password != self.connUser.ReturnUserPassword(self.userId):
            self.cautionPassword.setText('비밀번호가 맞지 않습니다.')
            self.cautionPassword.setVisible(True)
        elif self.approval in ['대기', '거절']:
            self.cautionAccount.setText('관리자의 승인이 필요합니다.')
            self.cautionAccount.setVisible(True)
        else:
            self.inputUserId.setText('')
            self.inputPassword.setText('')
            self.author = self.connUser.ReturnUserAuthor(self.userId)
            self.close()

    def btnSignupClick(self):
        dig = DialogSignUp()
        dig.exec_()

    def __layout__(self):
        layoutHorizontalCenter = QVBoxLayout()
        layoutHorizontalCenter.addWidget(self.img)
        layoutHorizontalCenter.addWidget(self.inputUserId)
        layoutHorizontalCenter.addWidget(self.cautionUserId)
        layoutHorizontalCenter.addWidget(self.inputPassword)
        layoutHorizontalCenter.addWidget(self.cautionPassword)
        layoutHorizontalCenter.addLayout(self.layoutBtn)
        layoutHorizontalCenter.addWidget(self.cautionAccount)
        layoutHorizontalCenter.addWidget(self.btnSignup)
        layoutHorizon = QHBoxLayout()
        layoutHorizon.addWidget(QLabel(), 3)
        layoutHorizon.addLayout(layoutHorizontalCenter, 0)
        layoutHorizon.addWidget(QLabel(), 3)
        layoutVertical = QVBoxLayout()
        layoutVertical.addWidget(QLabel(), 1)
        layoutVertical.addLayout(layoutHorizon, 3)
        layoutVertical.addWidget(QLabel(), 1)
        layoutVertical.addWidget(self.logo)
        layoutVertical.addWidget(QLabel(), 0)
        self.setLayout(layoutVertical)
