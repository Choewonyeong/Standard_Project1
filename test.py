from PyQt5.QtWidgets import QApplication
from component.dialog.DialogOther import DialogOther
from sys import argv
from PyQt5.QtWidgets import *


class GroupBoxBusiness(QGroupBox):
    def __init__(self, parent=None):
        QGroupBox.__init__(self, parent)
        self.__component__()

    def __component__(self):
        self.__default__()
        self.__layout__()

    def __default__(self):
        self.objectLabel = [QLabel('사업명'),
                            QLabel('기초가격'),
                            QLabel('고시금액'),
                            QLabel('낙찰율 감소 범위 값'),
                            QLabel('추첨율(상한)'),
                            QLabel('추첨율(하한)')]
        self.objectLineEdit = [QLineEdit(),     # 사업명
                               QLineEdit(),     # 기초가격
                               QLineEdit(),     # 고시가격
                               QLineEdit(),     # 낙찰율 감소율
                               QLineEdit(),     # 추첨율(상한)
                               QLineEdit()]     # 추첨율(하한)
        self.objectCaution = [QLabel('사업명을 입력하세요.'),
                              QLabel('기초가격을 입력하세요.'),
                              QLabel('고시금액을 입력하세요.'),
                              QLabel('낙찰율 감소 범위 값을 입력하세요.'),
                              QLabel('추첨율(상한)을 입력하세요.'),
                              QLabel('추첨율(하한)을 입력하세요.')]

    def __layout__(self):
        layout = QVBoxLayout()
        for lbl, ldt, caution in zip(self.objectLabel, self.objectLineEdit, self.objectCaution):
            layout.addWidget(lbl)
            layout.addWidget(ldt)
            layout.addWidget(caution)
            caution.setVisible(False)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(argv)
    test = GroupBoxBusiness()
    test.show()
    app.exec_()