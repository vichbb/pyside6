from PySide6.QtWidgets import QApplication, QWidget,QMainWindow, QLineEdit, QVBoxLayout
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        mainLayout = QVBoxLayout()
        line = QLineEdit(self)
        line.setPlaceholderText('请输入文本')
        mainLayout.addWidget(line)
        self.setLayout(mainLayout)




if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()