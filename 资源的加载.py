from PySide6.QtCore import QFile
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout,QLabel
import 资源文件_rc

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel()

        self.label.setPixmap(QPixmap(':image/111.png'))
        self.label.setScaledContents(True)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.label)
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()