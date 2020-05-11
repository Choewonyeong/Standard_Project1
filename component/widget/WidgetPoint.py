from PyQt5.QtWidgets import *

# 넘겨받아야할 인자
"""
넘겨받아야할 인자
= 있을 경우, lineEdit 에 값을 넘겨줄 것
= 없을 경우, pass
** 가격을 넘겨주는 게 아니라 차이범위를 넘겨줌으로써 하한가, 상한가를 구분해야 함.
= 선택한 값의 예정가격 (낙찰률을 100%라고 가정하고, 1%씩 깎으면서, 가격, 신인도 총점
"""


class WidgetPoint(QWidget):

    itemOption = ['기술용역적격심사']
    itemCriteria = ['(주)한국수력원자력']

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
        self.layoutBtnTop = QHBoxLayout()
        self.layoutBtnTop.addWidget(btnRun)
        self.layoutBtnTop.addWidget(Save)

    def __label__(self):
        self.lblPrice = QLabel()

    def __comboBox__(self):
        self.cbxOption = QComboBox()
        self.cbxOption.addItems(self.itemOption)
        self.cbxCriteria = QComboBox()
        self.cbxCriteria.addItems(self.itemCriteria)

    def __lineEdit__(self):
        self.lineEditPrice = QLineEdit()
        # 입력 이벤트 연결(원화 단위로)
        self.lineEditPlusRate = QLineEdit()
        self.lineEditMinusRate = QLineEdit()

    def __groupBox__(self):
        layoutSelf = QVBoxLayout()
        layoutSelf.addWidget(QLabel('예비가격기초금액'))     # 이게 예비가격기초금액을 의미하는지?
        layoutSelf.addWidget(self.lineEditPrice)
        layoutSelf.addWidget(QLabel('상한율'))
        layoutSelf.addWidget(self.lineEditPlusRate)
        layoutSelf.addWidget(QLabel('하한율'))
        layoutSelf.addWidget(self.lineEditMinusRate)
        layout = QVBoxLayout()
        layout.addLayout(self.layoutBtnTop)
        layout.addLayout(layoutSelf)

        layout.addWidget(QLabel(''), 10)
        self.groupBox = QGroupBox()
        self.groupBox.setLayout(layout)
        self.groupBox.setFixedWidth(230)

    def __tab__(self):
        self.tab = QTabWidget()

    def __layout__(self):
        layout = QHBoxLayout()
        layout.addWidget(self.groupBox)
        layout.addWidget(self.tab)
        self.setLayout(layout)
