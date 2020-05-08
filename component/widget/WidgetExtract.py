from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from pandas import ExcelWriter

from component.method import Transfer as Tran
from component.tab.TabExtract import TabExtract


class WidgetExtract(QWidget):

    runCount = 0

    def __init__(self):
        QWidget.__init__(self)
        self.__component__()

    def __component__(self):
        self.__button__()
        self.__label__()
        self.__lineEdit__()
        self.__comboBox__()
        self.__groupBox__()
        self.__tab__()
        self.__layout__()

    def __button__(self):
        btnRun = QPushButton('실행')
        btnRun.clicked.connect(self.btnRunClick)
        btnSave = QPushButton('엑셀로 저장')
        btnSave.clicked.connect(self.btnSaveClick)
        self.layoutBtnTop = QHBoxLayout()
        self.layoutBtnTop.addWidget(btnRun)
        self.layoutBtnTop.addWidget(btnSave)
        btnReset = QPushButton('초기화')
        btnApply = QPushButton('적용')
        self.layoutBtnBottom = QHBoxLayout()
        self.layoutBtnBottom.addWidget(btnReset)
        self.layoutBtnBottom.addWidget(btnApply)

    def btnRunClick(self):
        cntLoop = Tran.TransferCntLoop(self.lineEditCntLoop.text(), self.cautionCntLoop)
        price = Tran.TransferPrice(self.lineEditPrice.text(), self.cautionPrice)
        ratePlus = Tran.TransferRatePlus(self.lineEditRatePlus.text(), self.cautionRatePlus)/100
        rangePlus = int(int(price)+int(price)*float(ratePlus))
        cntPlus = Tran.TransferCntPlus(self.lineEditCntPlus.text(), self.cautionCntPlus)
        rateMinus = Tran.TransferRateMinus(self.lineEditRateMinus.text(), self.cautionRateMinus)/100
        rangeMinus = int(int(price)-int(price)*float(rateMinus))
        cntMinus = Tran.TransferCntMinus(self.lineEditCntMinus.text(), self.cautionCntMinus)
        rangeGap = float(self.cbxRangeGap.currentText())
        cntTotal = Tran.TransferCntTotal(self.lineEditCntTotal.text(), self.cautionCntTotal)
        options = [cntLoop,
                   price,
                   ratePlus,
                   rangePlus,
                   cntPlus,
                   rateMinus,
                   rangeMinus,
                   cntMinus,
                   rangeGap,
                   cntTotal]
        self.runCount += 1
        tabCount = self.tab.count()
        self.tab.addTab(TabExtract(options), f"실행-{self.runCount}회차")
        self.tab.setCurrentIndex(tabCount)

    def btnSaveClick(self):
        dig = QFileDialog(self)
        filePath = dig.getSaveFileName(caption="엑셀로 저장", directory='', filter='*.xlsx')[0]
        if filePath != '':
            with ExcelWriter(filePath) as writer:
                currentTab = self.tab.currentWidget()
                dfResult = currentTab.dfResult
                dfResult.to_excel(writer, sheet_name="분석 내역", index=False)
                dfExtract = currentTab.dfExtract
                dfExtract.to_excel(writer, sheet_name="추출 내역", index=False)
            writer.close()

    def __label__(self):
        self.cautionCntLoop = QLabel()
        self.cautionPrice = QLabel()
        self.cautionRatePlus = QLabel()
        self.cautionCntPlus = QLabel()
        self.cautionRateMinus = QLabel()
        self.cautionCntMinus = QLabel()
        self.cautionCntTotal = QLabel()
        self.cautionCntLoop.setAlignment(Qt.AlignCenter)
        self.cautionPrice.setAlignment(Qt.AlignCenter)
        self.cautionRatePlus.setAlignment(Qt.AlignCenter)
        self.cautionCntPlus.setAlignment(Qt.AlignCenter)
        self.cautionRateMinus.setAlignment(Qt.AlignCenter)
        self.cautionCntMinus.setAlignment(Qt.AlignCenter)
        self.cautionCntTotal.setAlignment(Qt.AlignCenter)
        # self.cautionCntLoop.setStyleSheet()
        # self.cautionPrice.setStyleSheet()
        # self.cautionRatePlus.setStyleSheet()
        # self.cautionCntPlus.setStyleSheet()
        # self.cautionRateMinus.setStyleSheet()
        # self.cautionCntMinus.setStyleSheet()
        # self.cautionCntTotal.setStyleSheet()
        self.cautionCntLoop.setVisible(False)
        self.cautionPrice.setVisible(False)
        self.cautionRatePlus.setVisible(False)
        self.cautionCntPlus.setVisible(False)
        self.cautionRateMinus.setVisible(False)
        self.cautionCntMinus.setVisible(False)
        self.cautionCntTotal.setVisible(False)

    def __lineEdit__(self):
        self.lineEditCntLoop = QLineEdit()
        self.lineEditCntLoop.setText('100,000')
        self.lineEditCntLoop.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.lineEditCntLoop.textEdited.connect(self.formatNumber)
        self.lineEditPrice = QLineEdit()
        self.lineEditPrice.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.lineEditPrice.textEdited.connect(self.formatNumber)
        self.lineEditRatePlus = QLineEdit()
        self.lineEditRatePlus.setText('2.5')
        self.lineEditRatePlus.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.lineEditCntPlus = QLineEdit()
        self.lineEditCntPlus.setText('8')
        self.lineEditCntPlus.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.lineEditRateMinus = QLineEdit()
        self.lineEditRateMinus.setText('2.5')
        self.lineEditRateMinus.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.lineEditCntMinus = QLineEdit()
        self.lineEditCntMinus.setText('7')
        self.lineEditCntMinus.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.lineEditCntTotal = QLineEdit()
        self.lineEditCntTotal.setText('4')
        self.lineEditCntTotal.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

    def __comboBox__(self):
        rangeGaps = [str(i/10000) for i in [1, 2, 4, 5]]
        self.cbxRangeGap = QComboBox()
        self.cbxRangeGap.addItems(rangeGaps)
        self.cbxRangeGap.setCurrentIndex(3)

    def formatNumber(self, text):
        try:
            lineEdit = self.sender()
            number = int(text.replace(',', ''))
            lineEdit.setText(format(number, ','))
        except:
            pass

    def __groupBox__(self):
        layout = QVBoxLayout()
        layout.addLayout(self.layoutBtnTop)
        layout.addWidget(QLabel(''))
        layout.addWidget(QLabel('총 반복 횟수'))
        layout.addWidget(self.lineEditCntLoop)
        layout.addWidget(self.cautionCntLoop)
        layout.addWidget(QLabel('예비가격 기초금액'))
        layout.addWidget(self.lineEditPrice)
        layout.addWidget(self.cautionPrice)
        layout.addWidget(QLabel(''))
        layout.addWidget(QLabel('상한율'))
        layout.addWidget(self.lineEditRatePlus)
        layout.addWidget(self.cautionRatePlus)
        layout.addWidget(QLabel('상한범위 추첨수'))
        layout.addWidget(self.lineEditCntPlus)
        layout.addWidget(self.cautionCntPlus)
        layout.addWidget(QLabel(''))
        layout.addWidget(QLabel('하한율'))
        layout.addWidget(self.lineEditRateMinus)
        layout.addWidget(self.cautionRateMinus)
        layout.addWidget(QLabel('하한범위 추첨수'))
        layout.addWidget(self.lineEditCntMinus)
        layout.addWidget(self.cautionCntMinus)
        layout.addWidget(QLabel(''))
        layout.addWidget(QLabel('범위 증감율 설정'))
        layout.addWidget(self.cbxRangeGap)
        layout.addWidget(QLabel(''))
        layout.addWidget(QLabel('예정가액 추첨수'))
        layout.addWidget(self.lineEditCntTotal)
        layout.addWidget(self.cautionCntTotal)
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