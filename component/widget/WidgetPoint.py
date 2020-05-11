from PyQt5.QtWidgets import *

# 넘겨받아야할 인자
"""
넘겨받아야할 인자
= 선택한 값의 예정가격 (낙찰률을 100%라고 가정하고, 1%씩 깎으면서, 가격, 신인도 총점
"""


class WidgetAnalysisPoint(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.__component__()

    def __component__(self):
        self.__button__()
        self.__lineEdit__()
        self.__groupBox__()
        self.__tab__()
        self.__layout__()

    def __button__(self):
        btnRun = QPushButton('실행')
        Save = QPushButton('엑셀로 저장')
        self.layoutBtnTop = QVBoxLayout()
        self.layoutBtnTop.addWidget(btnRun)
        self.layoutBtnTop.addWidget(Save)
        btnReset = QPushButton('초기화')
        btnApply = QPushButton('적용')
        self.layoutBtnBottom = QVBoxLayout()
        self.layoutBtnBottom.addWidget(btnReset)
        self.layoutBtnBottom.addWidget(btnApply)

    def __lineEdit__(self):
        self.lineEditCntLoop = QLineEdit()
        self.lineEditPrice = QLineEdit()
        self.lineEditRatePlus = QLineEdit()
        self.lineEditCntPlus = QLineEdit()
        self.lineEditRateMinus = QLineEdit()
        self.lineEditCntMinus = QLineEdit()
        self.lineEditCntTotal = QLineEdit()

    def __groupBox__(self):
        layout = QFormLayout()
        layout.addItem(self.layoutBtnTop)
        layout.addRow(self.lineEditCntLoop)
        layout.addRow(self.lineEditPrice)
        layout.addRow(self.lineEditRatePlus)
        layout.addRow(self.lineEditCntPlus)
        layout.addRow(self.lineEditRateMinus)
        layout.addRow(self.lineEditCntMinus)
        layout.addRow(self.lineEditCntTotal)
        layout.addItem(self.layoutBtnBottom)
        self.groupBox = QGroupBox()
        self.groupBox.setLayout(layout)
        self.groupBox.setFixedWidth(150)

    def __tab__(self):
        self.tab = QTabWidget()

    def __layout__(self):
        layout = QHBoxLayout()
        layout.addWidget(self.groupBox)
        layout.addWidget(self.tab)
        self.setLayout(layout)