from PySide6.QtWidgets import QApplication, QMainWindow,QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton('按钮', self)
        # self.setWindowTitle('基础框架')
        # self.resize(300, 300)
        btn.setGeometry(0, 0, 200, 100)
        btn.setToolTip('这是一个按钮')
        btn.setText('我被重新设置了')

if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()