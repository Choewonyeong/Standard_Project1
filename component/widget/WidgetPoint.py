from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from component.dialog.DialogTableOption import DialogTableOption
from component.dialog.DialogOther import DialogOther


class WidgetPoint(QWidget):

    itemOption = ['기술용역적격심사']
    itemCriteria = ['(주)한국수력원자력']
    otherInfo = {}

    def __init__(self):
        QWidget.__init__(self)
        self.total = 0
        self.dig = DialogOther()
        self.__component__()

    def __component__(self):
        self.__button__()
        self.__lineEditMain__()
        self.__lineEditSelf__()
        self.__groupBoxOther__()
        self.__groupBox__()
        self.__tab__()
        self.__layout__()

    def __button__(self):
        btnRun = QPushButton('실행')
        Save = QPushButton('엑셀로 저장')
        self.layoutBtnTop = QHBoxLayout()
        self.layoutBtnTop.addWidget(btnRun)
        self.layoutBtnTop.addWidget(Save)
        self.btnSubPoint = QPushButton('항목')
        self.btnSubPoint.clicked.connect(self.BtnSubPointClick)
        self.btnOther = QPushButton('경쟁사 정보\n업체명/기술(PQ)환산/신인도')
        self.btnOther.clicked.connect(self.BtnOtherClick)

    def BtnSubPointClick(self):
        dig = DialogTableOption()
        dig.exec_()
        self.total = dig.total
        self.lineEditSubPoint.setText(str(self.total))

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
        self.groupBoxMain = QGroupBox('사업 정보 입력')
        self.groupBoxMain.setLayout(layoutMain)

    def formatPriceMain(self, text):
        try:
            lineEdit = self.sender()
            price = int(text.replace(',', ''))
            lineEdit.setText(format(price, ','))
            self.dig.priceMain = price
        except:
            self.dig.priceMain = 0
            pass

    def formatPriceSub(self, text):
        try:
            lineEdit = self.sender()
            price = int(text.replace(',', ''))
            lineEdit.setText(format(price, ','))
            self.dig.priceSub = price
        except:
            self.dig.priceSub = 0
            pass

    def __lineEditSelf__(self):
        self.lineEditPriceSelf = QLineEdit()
        self.lineEditPlusRate = QLineEdit()
        self.lineEditMinusRate = QLineEdit()
        self.lineEditSubPoint = QLineEdit()
        self.lineEditSubPoint.setEnabled(False)
        self.lineEditSubPoint.setAlignment(Qt.AlignCenter)
        layoutSubPoint = QHBoxLayout()
        layoutSubPoint.addWidget(self.btnSubPoint)
        layoutSubPoint.addWidget(self.lineEditSubPoint)
        layoutSelf = QVBoxLayout()
        layoutSelf.addWidget(QLabel('예정가(추첨)'))
        layoutSelf.addWidget(self.lineEditPriceSelf)
        layoutSelf.addWidget(QLabel('예가율(상한율)'))
        layoutSelf.addWidget(self.lineEditPlusRate)
        layoutSelf.addWidget(QLabel('예가율(하한율)'))
        layoutSelf.addWidget(self.lineEditMinusRate)
        layoutSelf.addWidget(QLabel('신인도평가점수'))
        layoutSelf.addLayout(layoutSubPoint)
        self.groupBoxSelf = QGroupBox('우리 회사 정보 입력')
        self.groupBoxSelf.setLayout(layoutSelf)

    def __groupBoxOther__(self):
        self.listWidget = QListWidget()
        layoutOther = QVBoxLayout()
        layoutOther.addWidget(self.btnOther)
        layoutOther.addWidget(self.listWidget)
        self.groupBoxOther = QGroupBox('경쟁사 정보 입력')
        self.groupBoxOther.setLayout(layoutOther)

    def __groupBox__(self):
        layout = QVBoxLayout()
        layout.addLayout(self.layoutBtnTop)
        layout.addWidget(self.groupBoxMain)
        layout.addWidget(self.groupBoxSelf)
        layout.addWidget(self.groupBoxOther)
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
