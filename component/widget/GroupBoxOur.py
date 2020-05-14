from PyQt5.QtWidgets import *


class GroupBoxOur(QGroupBox):
    def __init__(self, parent=None):
        QGroupBox.__init__(self, parent)
        self.setTitle('우리 회사 정보')
        self.setVisible(False)
        self.__component__()

    def __component__(self):
        self.__default__()
        self.__groupBox__()
        self.__layout__()

    def __default__(self):
        self.objectLabel = [QLabel('기술(PQ) 점수'),
                            QPushButton('신인도평가점수'),
                            QLabel('기준비율'),
                            QLabel('최근년도 자기자본'),
                            QLabel('최근년도 총자산'),
                            QLabel('최근년도 유동자산'),
                            QLabel('최근년도 유동부채')]
        self.objectLineEdit = [QLineEdit(),     # 기술(PQ) 점수
                               QLineEdit(),     # 신인도평가점수
                               QLineEdit(),     # 기준비율
                               QLineEdit(),     # 최근년도 자기자본
                               QLineEdit(),     # 최근년도 총자산
                               QLineEdit(),     # 최근년도 유동자산
                               QLineEdit()]     # 최근년도 유동부채

    def __groupBox__(self):
        layout = QVBoxLayout()
        for idx in range(2, 7):
            layout.addWidget(self.objectLabel[idx])
            layout.addWidget(self.objectLineEdit[idx])
        self.gbxManagement = QGroupBox('경영 상태')
        self.gbxManagement.setVisible(False)
        self.gbxManagement.setLayout(layout)

    def __layout__(self):
        layout = QVBoxLayout()
        for idx in range(0, 2):
            layout.addWidget(self.objectLabel[idx])
            layout.addWidget(self.objectLineEdit[idx])
        layout.addWidget(self.gbxManagement)
        self.setLayout(layout)

