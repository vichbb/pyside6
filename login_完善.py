from PySide6.QtWidgets import QApplication, QWidget,QMainWindow, QLabel, QVBoxLayout
from Ui_登录框 import Ui_Form


# 方法2
class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.loginFunc)

    def loginFunc(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if username == 'admin' and password == '123456':
            print('登录成功')
        else:
            print('登录失败')

if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()
