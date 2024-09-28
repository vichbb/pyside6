from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.resize(400,300)
        
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        
        self.openFileAction = QAction("打开文件")
        self.closeFileAction = QAction("关闭文件")
        
        # self.addAction(self.openFileAction)
        # self.addAction(self.closeFileAction)
        self.addActions([self.openFileAction,self.closeFileAction])
        
        self.openFileAction.triggered.connect(lambda: print("打开文件"))
        self.closeFileAction.triggered.connect(lambda: print("关闭文件"))
        
        
        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)




if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()