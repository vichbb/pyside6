from PySide6.QtWidgets import QApplication, QWidget,QPushButton, QLineEdit, QVBoxLayout
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        mainLayout = QVBoxLayout()
        button = QPushButton('按钮')
        button.clicked.connect(self.onButtonClicked)

      
        mainLayout.addWidget(button)
        self.setLayout(mainLayout)

    def onButtonClicked(self):
        print('按钮被点击')

if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()