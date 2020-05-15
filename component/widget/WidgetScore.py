from PyQt5.QtWidgets import *
from component.widget.GroupBoxBusiness import GroupBoxBusiness
from component.widget.GroupBoxOur import GroupBoxOur
from component.widget.GroupBoxOtherPQ import GroupBoxOtherPQ
from component.widget.GroupBoxOtherManagement import GroupBoxOtherManagement
from component.dialog.DialogTableOption import DialogTableOption
from component.method.RunScoreCaseOne import RunScoreCaseOne
from component.method.RunScoreCaseTwo import RunScoreCaseTwo
from component.method.RunScoreCaseThree import RunScoreCaseThree
from component.method.RunScoreCaseFour import RunScoreCaseFour
from component.tab.TabScore import TabScore
from component.widget.WidgetTables import WidgetTables
from component.method.CreateDataFrame import CreateScoreCaseOne
from pandas import ExcelWriter


class WidgetScore(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.__variables__()
        self.__component__()

    def __variables__(self):
        self.title = ''
        self.priceMain = 0
        self.priceSub = 100000000   # 건축사법에 따른 설계는 5억원미만 1억원이상
        self.rateReduce = 0.001      # 1%
        self.priceHigh = 0
        self.priceLow = 0
        self.PQ = 0
        self.point = 0
        self.manage = 0
        self.rateStd = 0
        self.capital = 0
        self.asset = 0
        self.flowAsset = 0
        self.flowFan = 0

    def __component__(self):
        self.__button__()
        self.__default__()
        self.__groupBox__()
        self.__tab__()
        self.__layout__()
        self.__event__()

    def __button__(self):
        btnRun = QPushButton('실행')
        btnSave = QPushButton('엑셀로 저장')
        btnRun.clicked.connect(self.RunAnalysis)
        btnSave.clicked.connect(self.SaveToExcel)
        self.layoutBtn = QHBoxLayout()
        self.layoutBtn.addWidget(btnRun)
        self.layoutBtn.addWidget(btnSave)

    def RunAnalysis(self):
        try:
            if self.priceMain >= 1000000000:
                otherInfo = self.objectGroupBox[2].otherInfo
                names, dataFrames = CreateScoreCaseOne(self.priceMain, self.priceHigh, self.priceLow,
                                                       self.PQ, self.rateReduce, self.point, otherInfo)
                self.tab.addTab(TabScore(names, dataFrames, '기술점수'), self.title)
            elif self.priceMain >= 500000000:
                run = RunScoreCaseTwo(self.priceMain, self.PQ, self.rateReduce, self.point)
                df = run.ReturnToDataFrame()
            elif self.priceMain >= self.priceSub:
                run = RunScoreCaseThree(self.priceMain, self.PQ, self.rateReduce, self.poin)
                df = run.ReturnToDataFrame()
            elif self.priceMain < self.priceSub:
                run = RunScoreCaseFour(self.priceMain, self.rateStd, self.capital, self.asset,
                                       self.flowAsset, self.flowFan, self.rateReduce, self.point)
                df = run.ReturnToDataFrame()
        except Exception as e:
            print(e)

    def SaveToExcel(self):
        try:
            currentWidget = self.tab.currentWidget()
            dataFrames = currentWidget.dataFrames # [1][3]
            options = currentWidget.options # [3]
            names = currentWidget.names # [1]

            dig = QFileDialog(self)
            filePath = dig.getSaveFileName(caption="엑셀로 저장", directory='', filter='*.xlsx')[0]
            if filePath:
                with ExcelWriter(filePath) as writer:
                    for x, frames in enumerate(dataFrames):
                        for y, dataFrame in enumerate(frames):
                            dataFrame.to_excel(writer, sheet_name=f"{names[x]}-{options[y]}", index=False)
                writer.close()
        except Exception as e:
            print(e)

    def __default__(self):
        self.objectGroupBox = [GroupBoxBusiness(self),
                               GroupBoxOur(self),
                               GroupBoxOtherPQ(self),
                               GroupBoxOtherManagement(self)]
        self.valueReduce = [f"{round(num/10, 1)}%" for num in range(1, 1001)]
        self.objectGroupBox[0].objectLabel[2].setVisible(False)
        self.objectGroupBox[0].objectLineEdit[2].setVisible(False)
        self.objectGroupBox[0].objectLineEdit[3].addItems(self.valueReduce)

    def __groupBox__(self):
        layoutInput = QVBoxLayout()
        layoutInput.addLayout(self.layoutBtn)
        for gbx in self.objectGroupBox:
            layoutInput.addWidget(gbx)
        layoutInput.addWidget(QLabel(''), 10)
        self.gbxInput = QGroupBox()
        self.gbxInput.setLayout(layoutInput)
        self.gbxInput.setFixedWidth(230)

    def __tab__(self):
        self.tab = QTabWidget()

    def __layout__(self):
        layout = QHBoxLayout()
        layout.addWidget(self.gbxInput)
        layout.addWidget(self.tab)
        self.setLayout(layout)

    def __event__(self):
        self.objectGroupBox[0].objectLineEdit[0].textEdited.connect(self.getTitle)
        self.objectGroupBox[0].objectLineEdit[1].textEdited.connect(self.getPriceMain)
        self.objectGroupBox[0].objectLineEdit[2].textEdited.connect(self.getPriceSub)
        self.objectGroupBox[0].objectLineEdit[3].currentTextChanged.connect(self.getRateReduce)
        self.objectGroupBox[0].objectLineEdit[4].textEdited.connect(self.getPriceHigh)
        self.objectGroupBox[0].objectLineEdit[5].textEdited.connect(self.getPriceLow)
        self.objectGroupBox[1].objectLineEdit[0].textEdited.connect(self.getPQ)
        self.objectGroupBox[1].objectLabel[1].clicked.connect(self.getPoint)
        self.objectGroupBox[1].objectLineEdit[2].textEdited.connect(self.getRateStd)
        self.objectGroupBox[1].objectLineEdit[3].textEdited.connect(self.getCapital)
        self.objectGroupBox[1].objectLineEdit[4].textEdited.connect(self.getAsset)
        self.objectGroupBox[1].objectLineEdit[5].textEdited.connect(self.getflowAsset)
        self.objectGroupBox[1].objectLineEdit[6].textEdited.connect(self.getflowFan)

    def getTitle(self):
        self.title = self.sender().text()

    def getPriceMain(self):
        lineEdit = self.sender()
        priceText = lineEdit.text().replace(',', '')
        if priceText == '':
            self.objectGroupBox[0].info.setText('추정가격 : ')
            self.objectGroupBox[0].objectLabel[2].setVisible(False)
            self.objectGroupBox[0].objectLineEdit[2].setVisible(False)
            self.objectGroupBox[1].setVisible(False)
            self.objectGroupBox[1].gbxManagement.setVisible(False)
            self.objectGroupBox[2].setVisible(False)
            self.objectGroupBox[3].setVisible(False)
        try:
            self.priceMain = int(priceText)
            if self.priceMain >= 1000000000:
                self.objectGroupBox[0].info.setText('추정가격 : 10억원 이상')
                self.objectGroupBox[0].objectLabel[2].setVisible(False)
                self.objectGroupBox[0].objectLineEdit[2].setVisible(False)
                self.objectGroupBox[1].setVisible(True)
                self.objectGroupBox[1].gbxManagement.setVisible(False)
                self.objectGroupBox[2].setVisible(True)
                self.objectGroupBox[3].setVisible(False)
            elif self.priceMain >= 500000000:
                self.objectGroupBox[0].info.setText('추정가격 : 5억원 이상')
                self.objectGroupBox[0].objectLabel[2].setVisible(False)
                self.objectGroupBox[0].objectLineEdit[2].setVisible(False)
                self.objectGroupBox[1].setVisible(True)
                self.objectGroupBox[1].gbxManagement.setVisible(False)
                self.objectGroupBox[2].setVisible(True)
                self.objectGroupBox[3].setVisible(False)
            elif self.priceMain >= self.priceSub:
                self.objectGroupBox[0].info.setText('추정가격 : 고시금액 이상')
                self.objectGroupBox[0].objectLabel[2].setVisible(True)
                self.objectGroupBox[0].objectLineEdit[2].setVisible(True)
                self.objectGroupBox[1].setVisible(True)
                self.objectGroupBox[1].gbxManagement.setVisible(False)
                self.objectGroupBox[2].setVisible(True)
                self.objectGroupBox[3].setVisible(False)
            elif self.priceMain < self.priceSub:
                self.objectGroupBox[0].info.setText('추정가격 : 고시금액 미만')
                self.objectGroupBox[0].objectLabel[2].setVisible(True)
                self.objectGroupBox[0].objectLineEdit[2].setVisible(True)
                self.objectGroupBox[1].setVisible(True)
                self.objectGroupBox[1].gbxManagement.setVisible(True)
                self.objectGroupBox[2].setVisible(False)
                self.objectGroupBox[3].setVisible(True)
            priceText = format(self.priceMain, ',')
            lineEdit.setText(priceText)
        except:
            self.priceMain = 0

    def getPriceSub(self):
        lineEdit = self.sender()
        priceText = lineEdit.text().replace(',', '')
        try:
            self.priceSub = int(priceText)
            if self.priceSub < 100000000:
                self.priceSub = 100000000
            priceText = format(self.priceSub, ',')
            lineEdit.setText(priceText)
        except:
            self.priceSub = 100000000

    def getRateReduce(self, text):
        rateText = text.replace('%', '')
        try:
            self.rateReduce = round(float(rateText)/100, 3)
        except:
            self.rateReduce = 0

    def getPriceHigh(self):
        lineEdit = self.sender()
        priceText = lineEdit.text().replace(',', '')
        label = self.objectGroupBox[0].objectLabel[4]
        try:
            self.priceHigh = int(priceText)
            priceText = format(self.priceHigh, ',')
            lineEdit.setText(priceText)
            label.setText(f'추첨가격(상한)[추첨율 : {round(self.priceHigh/self.priceMain, 4)}]')
        except:
            self.priceHigh = 0
        if self.priceHigh != 0:
            label.setText(f'추첨가격(상한)[추첨율 : {round(self.priceHigh/self.priceMain, 4)}]')
        else:
            label.setText(f'추첨가격(상한)')

    def getPriceLow(self):
        lineEdit = self.sender()
        priceText = lineEdit.text().replace(',', '')
        label = self.objectGroupBox[0].objectLabel[5]
        try:
            self.priceLow = int(priceText)
            priceText = format(self.priceLow, ',')
            lineEdit.setText(priceText)
        except:
            self.priceLow = 0
        if self.priceLow != 0:
            label.setText(f'추첨가격(하한)[추첨율 : {round(self.priceLow/self.priceMain, 4)}]')
        else:
            label.setText(f'추첨가격(하한)')

    def getPQ(self):
        self.PQ = round(float(self.sender().text()), 3)

    def getPoint(self):
        lineEdit = self.objectGroupBox[1].objectLineEdit[1]
        try:
            dig = DialogTableOption()
            dig.exec_()
            self.point = dig.total
        except:
            self.point = 0
        lineEdit.setText(str(self.point))

    def getRateStd(self):
        lineEdit = self.sender()
        rateText = lineEdit.text().replace('%', '')
        try:
            self.rateStd = round(float(rateText)/100, 3)
        except:
            self.rateStd = 0

    def getCapital(self):
        lineEdit = self.sender()
        priceText = lineEdit.text().replace(',', '')
        try:
            self.capital = int(priceText)
            priceText = format(self.capital, ',')
            lineEdit.setText(priceText)
        except:
            self.capital = 0

    def getAsset(self):
        lineEdit = self.sender()
        priceText = lineEdit.text().replace(',', '')
        try:
            self.asset = int(priceText)
            priceText = format(self.asset, ',')
            lineEdit.setText(priceText)
        except:
            self.asset = 0

    def getflowAsset(self):
        lineEdit = self.sender()
        priceText = lineEdit.text().replace(',', '')
        try:
            self.flowAsset = int(priceText)
            priceText = format(self.flowAsset, ',')
            lineEdit.setText(priceText)
        except:
            self.flowAsset = 0

    def getflowFan(self):
        lineEdit = self.sender()
        priceText = lineEdit.text().replace(',', '')
        try:
            self.flowFan = int(priceText)
            priceText = format(self.flowFan, ',')
            lineEdit.setText(priceText)
        except:
            self.flowFan = 0


if __name__ == "__main__":
    from sys import argv
    app = QApplication(argv)
    test = WidgetScore()
    test.show()
    app.exec_()