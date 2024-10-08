import time

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel


class WorkThread(QThread):
    signal = Signal(str)

    def __init__(self):
        super().__init__()
        print("WorkThread init")

    def run(self):
        for i in range(10):
            self.signal.emit(str(i))
            print(f"WorkThread emit:{i}")
            time.sleep(1)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.lb = QLabel('当前值为:0')

        self.workThread = WorkThread()
        self.threadList = QThread()
        self.workThread.moveToThread(self.threadList)
        self.threadList.started.connect(self.workThread.run)
        self.threadList.finished.connect(lambda :print("WorkThread finished"))
        self.threadList.start()


        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lb)
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()