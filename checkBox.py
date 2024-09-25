from PySide6.QtWidgets import QApplication, QWidget,QCheckBox,QPushButton, QVBoxLayout
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        mainLayout = QVBoxLayout()
        checkBox = QCheckBox('是否被选中')
        checkBox.stateChanged.connect(self.showName)
        btn = QPushButton('按钮')
        btn.clicked.connect(lambda:print(checkBox.isChecked()))
        mainLayout.addWidget(btn)
        mainLayout.addWidget(checkBox)
        self.setLayout(mainLayout)
        
    def showName(self,name):
        print(name)
        

if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()