from PyQt5.QtWidgets import QApplication
from component.Loading import Loading
from sys import argv


if __name__ == "__main__":
    app = QApplication(argv)
    loading = Loading()
    loading.show()
    from component.Login import Login
    from component.Windows import Windows
    from connector.ConnUser import ConnUser
    connUser = ConnUser()
    userIds = connUser.ReturnUserIds()
    login = Login()
    login.show()
    loading.finish(login)
    app.exec_()
    if login.userId in userIds:
        windows = Windows(login.userId, login.author)
        windows.show()
        app.exec_()