from PyQt5.QtWidgets import *
from setting.Connector import connector
from component.dialog.DialogUserSelf import DialogUserSelf
from component.dialog.DialogAdminUser import DialogAdminUser
from component.dialog.DialogSignUpList import DialogSignUpList
from component.widget.WidgetSetup import WidgetSetup
from component.widget.WidgetExtract import WidgetExtract
from component.widget.WidgetScore import WidgetScore


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
            if text in self.currentTabs:
                self.tab.setCurrentIndex(self.currentTabs.index(text))
            elif text == self.mainItems[0]:
                self.tab.addTab(WidgetExtract(), text)
                self.currentTabs.append(text)
            elif text == self.mainItems[1]:
                self.tab.addTab(WidgetScore(), text)
                self.currentTabs.append(text)
            elif text == self.mainItems[2]:
                self.tab.addTab(WidgetSetup(self.userId, self.author), text)
                self.currentTabs.append(text)
            self.tab.setCurrentIndex(tabCounts)
        except Exception as e:
            print(e)

    def __tab__(self):
        self.tab = QTabWidget()

    def __layout__(self):
        layout = QHBoxLayout()
        layout.addWidget(self.mainList)
        layout.addWidget(self.tab)
        self.setLayout(layout)


