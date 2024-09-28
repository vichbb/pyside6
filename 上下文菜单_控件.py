from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout,QLineEdit,QPushButton,QMenu
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.resize(400,300)
        
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        
        self.openFileAction = QAction("打开文件")
        self.closeFileAction = QAction("关闭文件")
        self.addActions([self.openFileAction,self.closeFileAction])
        
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("输入框1")
        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setPlaceholderText("输入框2")
        
        # 对单个控件设置上下文菜单
        self.lineEdit.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        
        self.sendValueAction = QAction("发送值到输入框2")
        self.showCurrentValueAction = QAction("显示当前值")
        
        self.lineEdit.addActions([self.sendValueAction,self.showCurrentValueAction])
 
        
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lineEdit)
        self.mainLayout.addWidget(self.lineEdit2)
        self.setLayout(self.mainLayout)
        
        self.bindSlot()
        
    def bindSlot(self):
        self.openFileAction.triggered.connect(lambda: print("打开文件"))
        self.closeFileAction.triggered.connect(lambda: print("关闭文件"))
        self.sendValueAction.triggered.connect(lambda: self.lineEdit2.setText(self.lineEdit.text()))
        self.showCurrentValueAction.triggered.connect(lambda: print(self.lineEdit.text()))



if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()