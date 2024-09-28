from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout,QLineEdit,QPushButton,QLabel
from PySide6.QtCore import Signal


class MyWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.lineEditShow = QLineEdit()
        
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lineEditShow)
        self.setLayout(self.mainLayout)
        
        self.bind()
        
    def bind(self):
        self.subWindow = SubWindow(self)
        self.subWindow.show()
        
class SubWindow(QWidget):
    sendValueToMain = Signal(str)
    def __init__(self,parent=None):
        super().__init__()
        self.parent = parent
        self.move(20,20)
        
        self.lb = QLabel('子窗口')
        self.lineEditSub = QLineEdit()
        self.btn = QPushButton('发送数据到主窗口')
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lb)
        self.mainLayout.addWidget(self.lineEditSub)
        self.mainLayout.addWidget(self.btn)
        self.setLayout(self.mainLayout)
        self.bind()
 
    def bind(self):
        self.sendValueToMain.connect(self.parent.lineEditShow.setText)
        self.btn.clicked.connect(self.sendValue)

    def sendValue(self):
        self.sendValueToMain.emit(self.lineEditSub.text())

if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()