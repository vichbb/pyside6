from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout,QTextEdit,QPushButton,QFontDialog
from PySide6.QtGui import QFont

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.edit = QTextEdit()
        self.btn = QPushButton('点我设置字体')
        self.btn.clicked.connect(self.changeFont)
        
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.edit)
        self.mainLayout.addWidget(self.btn)
        self.setLayout(self.mainLayout)

    def changeFont(self):
        ok,font = QFontDialog.getFont()
        if ok and isinstance(font, QFont):  # 确保font是QFont实例
            self.edit.setFont(font)
        else:
            print(type(font))

if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()