from PyQt5.QtWidgets import *
from component.dialog.DialogOtherPQ import DialogOtherPQ


class GroupBoxOtherPQ(QGroupBox):
    def __init__(self, parent=None):
        QGroupBox.__init__(self, parent)
        self.setTitle('경쟁사 정보(기술점수)')
        self.setVisible(False)
        self.otherInfo = []
        self.__component__()

    def __component__(self):
        self.__default__()
        self.__layout__()

    def __default__(self):
        self.digOtherPQ = DialogOtherPQ(self)
        self.btnOtherPQ = QPushButton('경쟁사 정보 설정')
        self.btnOtherPQ.clicked.connect(self.BtnOtherPQClick)

    def BtnOtherPQClick(self):
        self.digOtherPQ.exec_()
        self.otherInfo = self.digOtherPQ.otherInfo

    def __layout__(self):
        layout = QVBoxLayout()
        layout.addWidget(self.btnOtherPQ)
        self.setLayout(layout)
