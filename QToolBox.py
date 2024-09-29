from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout,QToolBox,QLabel,QPushButton,QStyle

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # 创建一个右箭头图标和一个下箭头图标
        self.arrowRight = self.style().standardIcon(QStyle.StandardPixmap.SP_ArrowRight)
        self.arrowDown = self.style().standardIcon(QStyle.StandardPixmap.SP_ArrowDown)
        
        self.toolBox = QToolBox()
        
        #  创建折叠卡内容1
        self.widget1 = QWidget()
        self.widget1Layout = QVBoxLayout()
        self.widget1Layout.addWidget(QLabel("这是第1个选项卡"))
        self.widget1Layout.addWidget(QPushButton("按钮1"))
        self.widget1.setLayout(self.widget1Layout)
        
        #  创建折叠卡内容2
        self.widget2 = QWidget()
        self.widget2Layout = QVBoxLayout()
        self.widget2Layout.addWidget(QLabel("这是第2个选项卡"))
        self.widget2Layout.addWidget(QPushButton("按钮2"))
        self.widget2.setLayout(self.widget2Layout)
        
        #  创建折叠卡内容3
        self.widget3 = QWidget()
        self.widget3Layout = QVBoxLayout()
        self.widget3Layout.addWidget(QLabel("这是第3个选项卡"))
        self.widget3Layout.addWidget(QPushButton("按钮3"))
        self.widget3.setLayout(self.widget3Layout)
        
        self.toolBox.addItem(self.widget1,self.arrowRight, "选项卡1")
        self.toolBox.addItem(self.widget2,self.arrowRight, "选项卡2")
        self.toolBox.addItem(self.widget3,self.arrowRight, "选项卡3")
        
        self.toolBox.currentChanged.connect(self.onCurrentChanged)
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.toolBox)
        self.setLayout(self.mainLayout)
        
    def onCurrentChanged(self,index):
        for i in range(self.toolBox.count()):
            if i == index:
                self.toolBox.setItemIcon(i,self.arrowDown)
            else:
                self.toolBox.setItemIcon(i,self.arrowRight)


if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()