from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout,QMainWindow
from Ui_mainWindow import Ui_MainWindow

class MyWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 触发菜单栏的信号
        self.actionOpen.triggered.connect(lambda:self.statusbar.showMessage('打开文件'))
        self.actionSave.triggered.connect(lambda:self.statusbar.showMessage('保存文件'))
        self.actionExit.triggered.connect(lambda:self.statusbar.showMessage('退出窗口'))




if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()