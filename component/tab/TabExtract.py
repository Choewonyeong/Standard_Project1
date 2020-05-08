from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from component.method.RunExtract import RunExtract
from component.table.TableResult import TableResult
from component.table.TableExtract import TableExtract
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class TabExtract(QWidget):
    def __init__(self, options):
        QWidget.__init__(self)
        runExtract = RunExtract(options)
        self.columnsExtract, self.dfExtract = runExtract.ReturnExtract()
        self.columnsResult, self.dfResult, self.Indexes, self.dfSubResults = runExtract.ReturnResult()
        self.__component__()

    def __component__(self):
        self.__button__()
        self.__tblResult__()
        self.__canvasGraph__()
        self.__setTab__()
        self.__layout__()
        self.__drawCanvas__()

    def __button__(self):
        self.btnTexts = ["추출내역 확인", "추출내역 닫기"]
        self.btnShowExtract = QPushButton(self.btnTexts[0])
        self.btnShowExtract.clicked.connect(self.SetTblExtract)
        layout = QHBoxLayout()
        layout.addWidget(self.btnShowExtract)
        layout.addWidget(QLabel(), 10)
        self.groupBox = QGroupBox()
        self.groupBox.setLayout(layout)

    def SetTblExtract(self):
        if self.btnShowExtract.text() == self.btnTexts[0]:
            tblExtract = TableExtract(self.columnsExtract, self.dfExtract)
            self.tab.addTab(tblExtract, "추출내역")
            self.tab.setCurrentIndex(1)
            self.btnShowExtract.setText(self.btnTexts[1])
        elif self.btnShowExtract.text() == self.btnTexts[1]:
            self.tab.removeTab(1)
            self.btnShowExtract.setText(self.btnTexts[0])

    def __tblResult__(self):
        self.tblResult = TableResult(self.columnsResult, self.dfResult, self.Indexes)

    def __canvasGraph__(self):
        self.figure = plt.Figure()
        self.canvas = FigureCanvas(self.figure)
        self.navBar = NavigationToolbar(self.canvas, self)

    def __setTab__(self):
        layoutGraph = QVBoxLayout()
        layoutGraph.addWidget(self.navBar)
        layoutGraph.addWidget(self.canvas, 10)
        layoutResult = QHBoxLayout()
        layoutResult.addWidget(self.tblResult)
        layoutResult.addLayout(layoutGraph)
        groupBox = QGroupBox()
        groupBox.setLayout(layoutResult)
        self.tab = QTabWidget()
        self.tab.addTab(groupBox, "분석내역")

    def __layout__(self):
        layout = QVBoxLayout()
        layout.addWidget(self.groupBox)
        layout.addWidget(self.tab, 10)
        self.setLayout(layout)

    def __drawCanvas__(self):
        from matplotlib import font_manager
        fontLocation = "C:/Windows/fonts/malgun.ttf"
        fontName = font_manager.FontProperties(fname=fontLocation).get_name()
        plt.rc('font', family=fontName)
        plt.rcParams['font.size'] = 7
        columns, dfMaxCount, dfSubMaxCount = self.dfSubResults
        ax = self.figure.add_subplot(111)
        ax.barh(self.dfResult[columns[0]],
                self.dfResult[columns[1]],
                label=columns[1],
                linewidth=0.5,
                color='gray',
                edgecolor='black')
        ax.barh(dfMaxCount[columns[0]],
                dfMaxCount[columns[1]],
                label='최댓값',
                linewidth=0.5,
                color='red',
                edgecolor='black')
        ax.barh(dfSubMaxCount[columns[0]],
                dfSubMaxCount[columns[1]],
                label='상위5개항목',
                linewidth=0.5,
                color='blue',
                edgecolor='black')
        ax.legend(loc='upper right')
        plt.xticks(fontsize=7)
        plt.yticks(fontsize=7)
        self.figure.subplots_adjust(top=0.985, bottom=0.025)
        self.figure.set_edgecolor('black')
        self.figure.gca().invert_yaxis()
        self.canvas.draw()
