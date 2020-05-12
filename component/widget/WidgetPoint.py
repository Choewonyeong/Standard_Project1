from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from component.dialog.DialogTableOption import DialogTableOption
from component.dialog.DialogOther import DialogOther
from component.method.Score import TranPQScore


class WidgetPoint(QWidget):

    itemOption = ['기술용역적격심사']
    itemCriteria = ['(주)한국수력원자력']
    otherInfo = {}

    def __init__(self):
        QWidget.__init__(self)
        self.total = 0
        self.priceMain = 0
        self.priceSub = 0
        self.dig = DialogOther(self)
        self.__component__()

    def __component__(self):
        self.__button__()
        self.__lineEditMain__()
        self.__lineEditSelf__()
        self.__groupBoxOther__()
        self.__groupBoxSetting__()
        self.__groupBox__()
        self.__tab__()
        self.__layout__()

    def __button__(self):
        btnRun = QPushButton('실행')
        btnRun.clicked.connect(self.BtnRunClick)
        Save = QPushButton('엑셀로 저장')
        self.layoutBtnTop = QHBoxLayout()
        self.layoutBtnTop.addWidget(btnRun)
        self.layoutBtnTop.addWidget(Save)
        self.btnSubPoint = QPushButton('항목')
        self.btnSubPoint.clicked.connect(self.BtnSubPointClick)
        self.btnOther = QPushButton('경쟁사 정보\n업체명/기술(PQ)환산/신인도')
        self.btnOther.clicked.connect(self.BtnOtherClick)

    def BtnRunClick(self):
        pass

    def BtnSubPointClick(self):
        dig = DialogTableOption()
        dig.exec_()
        self.total = dig.total
        self.lineEditPoint.setText(str(self.total))

    def BtnOtherClick(self):
        self.dig.exec_()
        rowCount = self.dig.tblOther.rowCount()
        listItems = []
        deleteRows = []
        self.listWidget.clear()
        for row in range(rowCount):
            title = self.dig.tblOther.cellWidget(row, 0).text()
            rate = self.dig.tblOther.cellWidget(row, 2).text()
            point = self.dig.tblOther.cellWidget(row, 3).text()
            if title != "":
                listItems.append(f"{title} / {rate} / {point}")
            else:
                deleteRows.append(row)
        self.listWidget.addItems(listItems)
        deleteRows.sort(reverse=True)
        for row in deleteRows:
            self.dig.tblOther.removeRow(row)

    def __label__(self):
        self.lblPrice = QLabel()

    def __comboBox__(self):
        self.cbxOption = QComboBox()
        self.cbxOption.addItems(self.itemOption)
        self.cbxCriteria = QComboBox()
        self.cbxCriteria.addItems(self.itemCriteria)

    def __lineEditMain__(self):
        self.lineEditTitle = QLineEdit()
        self.lineEditPrice = QLineEdit()
        self.lineEditPrice.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.lineEditPrice.textEdited.connect(self.formatPriceMain)
        self.lineEditPriceSub = QLineEdit()
        self.lineEditPriceSub.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.lineEditPriceSub.textEdited.connect(self.formatPriceSub)
        # 입력 이벤트 연결(원화 단위로)
        layoutMain = QVBoxLayout()
        layoutMain.addWidget(QLabel('사업명'))
        layoutMain.addWidget(self.lineEditTitle)
        layoutMain.addWidget(QLabel('기초가격'))
        layoutMain.addWidget(self.lineEditPrice)
        layoutMain.addWidget(QLabel('고시금액'))
        layoutMain.addWidget(self.lineEditPriceSub)
        self.groupBoxMain = QGroupBox('사업 정보')
        self.groupBoxMain.setLayout(layoutMain)

    def formatPriceMain(self, text):
        try:
            lineEdit = self.sender()
            price = int(text.replace(',', ''))
            lineEdit.setText(format(price, ','))
            self.dig.priceMain = price
            self.priceMain = price
            self.formatScore(self.lineEditPQ.text())
        except:
            self.dig.priceMain = 0
            self.priceMain = 0
            self.formatScore(self.lineEditPQ.text())
            pass

    def formatPriceSub(self, text):
        try:
            lineEdit = self.sender()
            price = int(text.replace(',', ''))
            lineEdit.setText(format(price, ','))
            self.dig.priceSub = price
            self.priceSub = price
            self.formatScore(self.lineEditPQ.text())
        except:
            self.dig.priceSub = 0
            self.priceSub = 0
            self.formatScore(self.lineEditPQ.text())
            pass

    def __lineEditSelf__(self):
        self.lineEditPQ = QLineEdit()
        self.lineEditPQ.textChanged.connect(self.formatScore)
        self.lineEditPQTran = QLineEdit()
        self.lineEditPQTran.setEnabled(False)
        self.lineEditPoint = QLineEdit()
        self.lineEditPoint.setEnabled(False)
        self.lineEditPoint.setAlignment(Qt.AlignCenter)
        layoutSubPoint = QHBoxLayout()
        layoutSubPoint.addWidget(self.btnSubPoint)
        layoutSubPoint.addWidget(self.lineEditPoint)
        layoutSelf = QVBoxLayout()
        layoutSelf.addWidget(QLabel('기술(PQ)점수'))
        layoutSelf.addWidget(self.lineEditPQ)
        layoutSelf.addWidget(QLabel('기술(PQ)점수 환산'))
        layoutSelf.addWidget(self.lineEditPQTran)
        layoutSelf.addWidget(QLabel('신인도평가점수'))
        layoutSelf.addLayout(layoutSubPoint)
        self.groupBoxSelf = QGroupBox('우리 회사 정보')
        self.groupBoxSelf.setLayout(layoutSelf)

    def formatScore(self, text):
        try:
            score = round(float(text), 3)
            scoreTran = TranPQScore(self.priceMain, self.priceSub, score)
            self.lineEditPQTran.setText(str(scoreTran.__format__('.3f')))
        except:
            pass

    def __groupBoxOther__(self):
        self.listWidget = QListWidget()
        layoutOther = QVBoxLayout()
        layoutOther.addWidget(self.btnOther)
        layoutOther.addWidget(self.listWidget)
        self.groupBoxOther = QGroupBox('경쟁사 정보')
        self.groupBoxOther.setLayout(layoutOther)

    def __groupBoxSetting__(self):
        self.lineEditRateLimited = QLineEdit() # 낙찰하한율
        self.lineEditRateDistance = QLineEdit() # 낙찰율 감소범위
        self.lineEditMaxRate = QLineEdit() # 추첨상한율
        self.lineEditMinRate = QLineEdit() # 추첨하한율
        layoutSetting = QVBoxLayout()
        layoutSetting.addWidget(QLabel('낙찰하한율'))
        layoutSetting.addWidget(self.lineEditRateLimited)
        layoutSetting.addWidget(QLabel('낙찰율 감소범위'))
        layoutSetting.addWidget(self.lineEditRateDistance)
        layoutSetting.addWidget(QLabel('추첨상한율'))
        layoutSetting.addWidget(self.lineEditMaxRate)
        layoutSetting.addWidget(QLabel('추첨하한율'))
        layoutSetting.addWidget(self.lineEditMinRate)
        self.groupBoxSetting = QGroupBox('분석 설정')
        self.groupBoxSetting.setLayout(layoutSetting)

    def __groupBox__(self):
        layout = QVBoxLayout()
        layout.addLayout(self.layoutBtnTop)
        layout.addWidget(self.groupBoxMain)
        layout.addWidget(self.groupBoxSelf)
        layout.addWidget(self.groupBoxOther)
        layout.addWidget(self.groupBoxSetting)
        layout.addWidget(QLabel(''))
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
