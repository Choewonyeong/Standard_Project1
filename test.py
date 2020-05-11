from PyQt5.QtWidgets import QApplication
from component.dialog.DialogOther import DialogOther
from sys import argv


if __name__ == "__main__":
    app = QApplication(argv)
    test = DialogOther()
    test.show()
    app.exec_()