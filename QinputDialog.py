from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout,QInputDialog,QPushButton,QLineEdit

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        btn1 = QPushButton('获取一个整型数字')
        btn1.clicked.connect(self.getIntDialog)
        
        btn2 = QPushButton('获取一个浮点型数字')
        btn2.clicked.connect(self.getFloatDialog)
        
        
        btn3 = QPushButton('获取一个Item')
        btn3.clicked.connect(lambda : print(QInputDialog.getItem(self,'标题','请选择一个选项',['选项1','选项2','选项3'],0,False)))
        
        btn4 = QPushButton('获取一个单行文本')
        # 不回显模式
        # btn4.clicked.connect(lambda : print(QInputDialog.getText(self,'标题','请输入你的名字',QLineEdit.EchoMode.NoEcho,'默认值')))
        btn4.clicked.connect(lambda : print(QInputDialog.getText(self,'标题','请输入你的名字',QLineEdit.EchoMode.Normal,'默认值')))
                
        btn5 = QPushButton('获取一个多行文本')
        btn5.clicked.connect(lambda : print(QInputDialog.getMultiLineText(self,'标题','请输入你的名字')))
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(btn1)
        self.mainLayout.addWidget(btn2)
        self.mainLayout.addWidget(btn3)
        self.mainLayout.addWidget(btn4)
        self.mainLayout.addWidget(btn5)
        self.setLayout(self.mainLayout)
    def getIntDialog(self):
        # self,标题,提示,默认值,最小值,最大值,步长
        result,ok = QInputDialog.getInt(self,'标题','请输入一个整型数字',1,0,100,1)
        if ok:
            print(result)
        
        # QInputDialog.getDouble(self,'标题','请输入一个浮点型数字',100.0,0,1000,1)
        # QInputDialog.getItem(self,'标题','请选择一个选项',['选项1','选项2','选项3'])
        # QInputDialog.getText(self,'标题','请输入你的名字')

    def getFloatDialog(self):
        result,ok = QInputDialog.getDouble(self,'标题','请输入一个浮点型数字',1.0,0.0,100.0,1.0)
        if ok:
            print(result)

if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()