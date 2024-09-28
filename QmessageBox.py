from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout,QPushButton,QMessageBox

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.resize(400,300)
        self.btn = QPushButton('点击我')
        self.btn.clicked.connect(self.btnClicked)
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.btn)
        self.setLayout(self.mainLayout)
        
    def btnClicked(self):
        # 最后一个参数是默认按钮
        result = QMessageBox.information(self,'标题','这是一个消息框',QMessageBox.StandardButton.Ok|QMessageBox.StandardButton.Cancel|QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Ok)
        if result == QMessageBox.StandardButton.Ok:
            print('点击了OK')
        elif result == QMessageBox.StandardButton.Cancel:
            print('点击了Cancel')
        elif result == QMessageBox.StandardButton.Close:
            print('点击了Close')
        else:
            print('点击了其他按钮')
        
        
        # QMessageBox.question(self,'标题','这是一个问题框',QMessageBox.Yes|QMessageBox.No)
        # QMessageBox.warning(self,'标题','这是一个警告框')
        # QMessageBox.critical(self,'标题','这是一个错误框')
        # QMessageBox.about(self,'标题','这是一个关于框')
        




if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()