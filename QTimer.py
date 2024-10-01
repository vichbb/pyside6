from PIL import Image, ImageQt
from PIL.ImageQt import QPixmap
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.count = 0
        self.picList = ["./img/111.png","./img/wallhaven_57j6m7.jpg","./img/wallhaven_d65xxm.jpg","./img/wallhere-2103907.jpg"]

        self.timer = QTimer()
        self.timer.timeout.connect(self.changePic)

        QTimer.singleShot(1000,lambda :print("Hello World"))

        self.lb = QLabel()
        self.lb.setPixmap(QPixmap(self.picList[0]))

        self.btn = QPushButton("Start")
        self.btn.clicked.connect(lambda :self.timer.start(1000))

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lb)
        self.mainLayout.addWidget(self.btn)
        self.setLayout(self.mainLayout)

    def changePic(self):
        print("changePic")
        self.count += 1
        image = self.getResizeImage(Image.open(self.picList[self.count % self.picList.__len__()]))
        self.lb.setPixmap(ImageQt.toqpixmap(image))

#     resize图片
    def getResizeImage(self,img):
        width,height = img.size
        # newWidth = int(width*0.3)
        # newHeight = int(height*0.3)
        newWidth = int(800)
        newHeight = int(600)
        return img.resize((newWidth,newHeight))

if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()