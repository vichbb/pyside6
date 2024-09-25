from PySide6.QtWidgets import QApplication, QWidget,QComboBox, QVBoxLayout
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        mainLayout = QVBoxLayout()
        combo = QComboBox()
        combo.addItems(['item1', 'item2', 'item3'])
        # combo.currentTextChanged.connect(self.showName)
        combo.currentIndexChanged.connect(self.showName)
        mainLayout.addWidget(combo)
        self.setLayout(mainLayout)
        
    def showName(self,name):
        print(name)
        

if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()