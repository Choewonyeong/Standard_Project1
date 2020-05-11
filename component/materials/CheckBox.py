from PyQt5.QtWidgets import QCheckBox


class CheckBox(QCheckBox):
    def __init__(self):
        QCheckBox.__init__(self)
        style = "QCheckBox{margin-left: 10px; background-color: rgba(255, 255, 255, 10);} "
        self.setStyleSheet(style)
