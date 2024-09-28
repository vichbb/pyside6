from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout,QLineEdit,QPushButton,QLabel
from PySide6.QtCore import Signal


class MyWindow(QWidget):
    sendValueToSubWindow = Signal(str)
    
    def __init__(self):
        super().__init__()
        
        self.lineEditSend = QLineEdit()
        self.btn = QPushButton('发送数据到子窗口')
        
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lineEditSend)
        self.mainLayout.addWidget(self.btn)
        self.setLayout(self.mainLayout)
        
        self.bind()

    def bind(self):
        self.subWindow = SubWindow()
        self.sendValueToSubWindow.connect(self.subWindow.lineEditSub.setText)
        self.btn.clicked.connect(self.sendValue)
        self.subWindow.show()
        
    def sendValue(self):
        self.sendValueToSubWindow.emit(self.lineEditSend.text())
        
    
class SubWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.lb = QLabel('子窗口')
        
        # 接收
        self.lineEditSub = QLineEdit()
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lb)
        self.mainLayout.addWidget(self.lineEditSub)
        self.setLayout(self.mainLayout)
 



if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()