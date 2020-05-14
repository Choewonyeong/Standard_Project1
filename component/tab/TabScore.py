from PyQt5.QtWidgets import *
from component.widget.WidgetTables import WidgetTables
from component.table.TableScore import TableScore


class TabScore(QTabWidget):
    def __init__(self, nameTable, objectTable, priceHigh, priceLow):
        QWidget.__init__(self)
        self.nameTable = nameTable
        self.objectTable = objectTable
        self.priceHigh = priceHigh
        self.priceLow = priceLow
        self.__component__()

    def __component__(self):
        self.__table__()

