from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout,QLabel,QStyle


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.lb = QLabel()
        # self.lb.setPixmap(self.style().standardPixmap(QStyle.StandardPixmap.SP_DialogSaveButton))
        self.lb.setPixmap(self.style().standardPixmap(QStyle.StandardPixmap.SP_DesktopIcon))

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lb)
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()