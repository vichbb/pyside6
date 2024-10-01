import time

from PySide6.QtCore import QThread, Signal,QObject
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel


class WorkThread(QObject):
    signal = Signal(str)

    def __init__(self):
        super().__init__()
        print("WorkThread init")

    def run(self):
        for i in range(10):
            self.signal.emit(str(i))
            time.sleep(1)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.lb = QLabel('当前值为:0')



        self.workThread = WorkThread()
        self.workThread.signal.connect(lambda x:self.lb.setText(f'当前值为:{x}'))
        # self.workThread.finished.connect(lambda :print("WorkThread finished"))
        # 线程结束后自动删除子线程,释放内存
        self.workThread.finished.connect(self.workThread.deleteLater)
        self.workThread.start()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lb)
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()