from PySide6.QtWidgets import QApplication, QWidget , QVBoxLayout,QTextEdit,QPlainTextEdit,QPushButton
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        textEdit = QPlainTextEdit()
        # textEdit.setHtml('<h1>我是一个文本编辑器</h1>')
        # textEdit.setMarkdown('## 我是一个文本编辑器')
        textEdit.setPlainText('这是一个标题')
        textEdit.appendPlainText('这是一个段落')
        
        btn = QPushButton('追加文本')
        btn.clicked.connect(lambda : textEdit.appendPlainText('这是追加的文本'))
       
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(textEdit)
        self.mainLayout.addWidget(btn)
        self.setLayout(self.mainLayout)

if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()