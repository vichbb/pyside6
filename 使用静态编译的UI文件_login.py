from PySide6.QtWidgets import QApplication, QWidget,QMainWindow, QLabel, QVBoxLayout
from login import Ui_Form

# 方法1
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_Form()
#         self.ui.setupUi(self)

# if __name__ == "__main__":
#     app = QApplication([])
#     myWin = MyWindow()
#     myWin.show()
#     app.exec()

# 方法2
class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()
