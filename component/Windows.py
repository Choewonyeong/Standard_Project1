from PyQt5.QtWidgets import *
from setting.Connector import connector
from component.dialog.DialogUserSelf import DialogUserSelf
from component.dialog.DialogAdminUser import DialogAdminUser
from component.dialog.DialogSignUpList import DialogSignUpList
from component.widget.WidgetExtract import WidgetExtract


class Windows(QWidget):
    def __init__(self, userId, author):
        QWidget.__init__(self)
        self.connUser = connector[0]
        self.userId = userId
        self.author = author
        self.__setting__()
        self.__variables__()
        self.__component__()

    def __setting__(self):
        self.showMaximized()
        self.setWindowTitle('입찰가 및 적격심사점수 분석 프로그램 - (주)스탠더드시험연구소')

    def __variables__(self):
        self.currentTabs = []

    def __component__(self):
        self.__mainList__()
        self.__subList__()
        self.__tab__()
        self.__layout__()

    def __mainList__(self):
        self.mainItems = ['입찰가분석',
                          '적격심사분석',
                          '설정']
        self.mainList = QListWidget()
        self.mainList.addItems(self.mainItems)
        self.mainList.setFixedWidth(150)
        self.mainList.itemClicked.connect(self.mainListItemClick)

    def mainListItemClick(self, item):
        try:
            text = item.text()
            tabCounts = self.tab.count()
            if text in self.currentTabs and text != self.mainItems[2]:
                self.tab.setCurrentIndex(self.currentTabs.index(text))
                self.subList.setVisible(False)
            elif text in self.currentTabs and text == self.mainItems[2]:
                self.tab.setCurrentIndex(self.currentTabs.index(text))
                self.subList.setVisible(True)
            elif text == self.mainItems[0]:
                self.tab.addTab(WidgetExtract(), text)
                self.subList.setVisible(False)
                self.currentTabs.append(text)
            elif text == self.mainItems[1]:
                # 적격심사 분석 실행 탭 추가
                self.subList.setVisible(False)
                self.currentTabs.append(text)
            elif text == self.mainItems[2]:
                self.tab.addTab(QLabel(), text)
                self.subList.setVisible(True)
                self.currentTabs.append(text)
            self.tab.setCurrentIndex(tabCounts)
        except Exception as e:
            print(e)

    def __subList__(self):
        self.subList = QListWidget()
        self.subList.setFixedWidth(150)
        if self.author == '관리자':
            self.subListItem = ['비밀번호 설정',
                                '가입 신청 관리',
                                '회원 정보 관리']
        elif self.author == '사용자':
            self.subListItem = ['비밀번호 설정']
        self.subList.addItems(self.subListItem)
        self.subList.itemClicked.connect(self.subListItemClick)
        self.subList.setVisible(False)

    def subListItemClick(self, item):
        text = item.text()
        if text == self.subListItem[0]:
            dig = DialogUserSelf(self.userId)
            dig.exec_()
        elif text == self.subListItem[1]:
            dig = DialogSignUpList()
            dig.exec_()
        elif text == self.subListItem[2]:
            dig = DialogAdminUser()
            dig.exec_()

    def __tab__(self):
        self.tab = QTabWidget()

    def __layout__(self):
        layout = QHBoxLayout()
        layout.addWidget(self.mainList)
        layout.addWidget(self.subList)
        layout.addWidget(self.tab)
        self.setLayout(layout)


