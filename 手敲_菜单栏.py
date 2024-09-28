from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout,QMainWindow,QMenu,QStyle
from PySide6.QtGui import QAction
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu = self.menuBar()
    
        self.fileMenu = QMenu("文件")
        self.openFileAction = QAction(self.style().standardIcon(QStyle.StandardPixmap.SP_DirOpenIcon),"打开文件")
        self.closeFileAction = QAction(self.style().standardIcon(QStyle.StandardPixmap.SP_DirClosedIcon),"关闭文件")
        self.fileMenu.addAction(self.openFileAction)
        self.fileMenu.addAction(self.closeFileAction)
        
        self.moreMenu = QMenu("更多")
        self.moreAction1 = QAction("更多1")
        self.moreAction2 = QAction("更多2")
        self.moreMenu.addAction(self.moreAction1)
        self.moreMenu.addAction(self.moreAction2)
        self.fileMenu.addMenu(self.moreMenu)
        self.menu.addMenu(self.fileMenu)
        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)
        self.bindSlot()

    def bindSlot(self):
        self.openFileAction.triggered.connect(lambda: print("打开文件"))
        self.closeFileAction.triggered.connect(lambda: print("关闭文件"))
        self.moreAction1.triggered.connect(lambda: print("更多1"))
        self.moreAction2.triggered.connect(lambda: print("更多2"))


if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()