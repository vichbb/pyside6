from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout,QPushButton,QFileDialog

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        btn = QPushButton('打开文件')
        # self,标题,默认路径,过滤器
        # 过滤器格式: '所有文件(*);;python文件(*.py *.pyd)'
        # 返回值: (绝对文件路径,过滤类型)
        btn.clicked.connect(lambda : print(QFileDialog.getOpenFileName(self,'打开文件','.','All Files (*);;python Files (*.py *.pyd)')))
        
        # 返回值: (绝对文件路径列表,过滤类型)
        btn2 = QPushButton('打开多个文件')
        btn2.clicked.connect(lambda : print(QFileDialog.getOpenFileNames(self,'打开文件','.','All Files (*);;python Files (*.py *.pyd)')))

        btn3 = QPushButton('打开文件夹')
        # self,标题,默认路径
        # 返回值
        btn3.clicked.connect(lambda : print(QFileDialog.getExistingDirectory(self,'打开文件夹','.')))
        
        btn4 = QPushButton('保存文件')
        btn4.clicked.connect(lambda : print(QFileDialog.getSaveFileName(self,'保存文件','.','All Files (*);;python Files (*.py *.pyd)')))
                
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(btn)
        self.mainLayout.addWidget(btn2)
        self.mainLayout.addWidget(btn3)
        self.mainLayout.addWidget(btn4)
        self.setLayout(self.mainLayout)




if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()