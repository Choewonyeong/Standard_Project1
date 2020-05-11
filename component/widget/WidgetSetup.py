from PyQt5.QtWidgets import *
from component.dialog.DialogAdminUser import DialogAdminUser
from component.dialog.DialogSignUpList import DialogSignUpList
from component.dialog.DialogUserSelf import DialogUserSelf


class WidgetSetup(QWidget):

    listItem = ['비밀번호 설정',
                '가입 신청 관리',
                '회원 정보 관리']

    def __init__(self, userId, author):
        QWidget.__init__(self)
        self.userId = userId
        self.author = author
        self.__component__()

    def __component__(self):
        self.__listWidget__()
        self.__tab__()
        self.__layout__()

    def __listWidget__(self):
        self.listWidget = QListWidget()
        self.listWidget.setFixedWidth(150)
        if self.author == '관리자':
            self.listWidget.addItems(self.listItem)
        elif self.author == '사용자':
            self.listWidget.addItems(self.listItem[0:1])
        self.listWidget.itemClicked.connect(self.listItemClick)

    def listItemClick(self, item):
        text = item.text()
        if text == self.listItem[0]:
            dig = DialogUserSelf(self.userId)
            dig.exec_()
        elif text == self.listItem[1]:
            dig = DialogSignUpList()
            dig.exec_()
        elif text == self.listItem[2]:
            dig = DialogAdminUser()
            dig.exec_()

    def __tab__(self):
        self.tab = QTabWidget()

    def __layout__(self):
        layout = QHBoxLayout()
        layout.addWidget(self.listWidget)
        layout.addWidget(self.tab)
        self.setLayout(layout)

