from PyQt5.QtWidgets import QApplication
from component.table.TableOption import TableOption
from sys import argv


if __name__ == "__main__":
    app = QApplication(argv)
    TableOption = TableOption()
    TableOption.show()
    app.exec_()