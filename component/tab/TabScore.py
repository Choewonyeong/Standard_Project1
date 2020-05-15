from PyQt5.QtWidgets import *
from component.widget.WidgetTables import WidgetTables
from component.table.TableScore import TableScore


class TabScore(QTabWidget):
    def __init__(self, names, dataFrames, scoreType):
        QWidget.__init__(self)
        self.options = ['예비가', '상한가', '하한가']
        self.names = names
        self.dataFrames = dataFrames
        self.scoreType = scoreType
        self.__variables__()
        self.__widgets__()
        self.__setting__()

    def __variables__(self):
        try:
            self.tables = []
            for x, option in enumerate(self.options):
                tables = []
                for y, dataFrame in enumerate(self.dataFrames):
                    tables.append(TableScore(self.dataFrames[y][x], self.scoreType))
                self.tables.append(tables)
        except Exception as e:
            print('__variables__', e)

    def __widgets__(self):
        try:
            self.widgets = []
            for tables in self.tables:
                self.widgets.append(WidgetTables(self.names, tables))
        except Exception as e:
            print('__widgets__', e)

    def __setting__(self):
        try:
            for option, widget in zip(self.options, self.widgets):
                self.addTab(widget, option)
        except Exception as e:
            print('__setting__', e)

