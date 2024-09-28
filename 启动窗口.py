from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout,QLabel
from PySide6.QtCore import Qt,QTimer
from PySide6.QtGui import QFont


class LoadingWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.lb = QLabel('加载中...')
        self.lb.setFont(QFont('Microsoft YaHei',50))
        self.lb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lb)
        self.setLayout(self.mainLayout)
        
        QTimer.singleShot(3000,self.openMainWindow)
    def openMainWindow(self):
        self.close()
        self.mainWindow = MainWindow()
        self.mainWindow.show()
        
        
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('主窗口')
        
        self.lb = QLabel('欢迎使用本软件')
        self.lb.setFont(QFont('Microsoft YaHei',50))
        self.lb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lb)
        self.setLayout(self.mainLayout)
        
    def openMainWindow(self):
        self.mainWindow = MainWindow()
        self.mainWindow.show()
        self.close()



if __name__ == "__main__":
    app = QApplication([])
    myWin = LoadingWindow()
    myWin.show()
    app.exec()