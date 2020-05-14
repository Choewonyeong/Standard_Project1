from PyQt5.QtWidgets import *
from component.dialog.DialogOtherManagement import DialogOtherManagement


class GroupBoxOtherManagement(QGroupBox):
    def __init__(self, parent=None):
        QGroupBox.__init__(self, parent)
        self.setTitle('경쟁사 정보(경영점수)')
        self.setVisible(False)
        self.otherInfo = []
        self.__component__()

    def __component__(self):
        self.__default__()
        self.__layout__()

    def __default__(self):
        self.digOtherManagement = DialogOtherManagement(self)
        self.btnOtherManagement = QPushButton('경쟁사 정보(경영점수)')
        self.btnOtherManagement.clicked.connect(self.BtnOtherManagementClick)

    def BtnOtherManagementClick(self):
        self.digOtherManagement.exec_()
        self.otherInfo = self.digOtherManagement.otherInfo

    def __layout__(self):
        layout = QVBoxLayout()
        layout.addWidget(self.btnOtherManagement)
        self.setLayout(layout)
