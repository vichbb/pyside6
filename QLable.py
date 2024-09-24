from PySide6.QtWidgets import QApplication, QWidget,QMainWindow, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        mainLayout = QVBoxLayout()

        label = QLabel('我是一个标签', self)
        label.setText('我是被修改过的标签')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        mainLayout.addWidget(label)
        self.setLayout(mainLayout)

if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()