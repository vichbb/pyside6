from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout,QLabel,QLineEdit,QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.subWindow = SubWindow()
        
        self.lb = QLabel('主窗口')
        self.btn = QPushButton('打开子窗口')
        self.btn.clicked.connect(self.openSubWindow)
        
        self.btnClose = QPushButton('关闭子窗口')
        self.btnClose.clicked.connect(self.closeSubWindow)
        
        self.btnHide = QPushButton('隐藏子窗口')
        self.btnHide.clicked.connect(self.hideSubWindow)
        
        
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lb)
        self.mainLayout.addWidget(self.btn)
        self.mainLayout.addWidget(self.btnClose)
        self.mainLayout.addWidget(self.btnHide)
        self.setLayout(self.mainLayout)
    def openSubWindow(self):
        self.subWindow.show()
        
    def closeSubWindow(self):
        self.subWindow.close()
        
    def hideSubWindow(self):
        self.subWindow.hide()

class SubWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.lb = QLabel('子窗口')
        self.lineEdit = QLineEdit()
        self.lineEdit.setText('子窗口的文本')
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lb)
        self.mainLayout.addWidget(self.lineEdit)
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()