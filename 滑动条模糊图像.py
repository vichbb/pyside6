from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout,QSlider,QFileDialog,QPushButton,QLabel
from PySide6.QtCore import Qt
from PIL import Image,ImageFilter,ImageQt
from PySide6.QtGui import QPixmap

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.btn = QPushButton('点我导入图像')
        self.btn.clicked.connect(self.getImage)
        
        self.lbShowImage = QLabel()
        
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0,20)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(3)
        self.slider.valueChanged.connect(self.sliderValueChanged)
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lbShowImage)
        self.mainLayout.addWidget(self.slider)
        self.mainLayout.addWidget(self.btn)
        self.setLayout(self.mainLayout)

    def getImage(self):
        self.img = Image.open(QFileDialog.getOpenFileName(self,'打开文件','.','JPG Files (*.jpg);;PNG Files (*.png)')[0])
        # resize 图像适应屏幕
        self.img = self.getResizeImage(self.img)
        self.lbShowImage.setPixmap(ImageQt.toqpixmap(self.img))

    def sliderValueChanged(self,value):
        self.blurImage = self.img.filter(ImageFilter.GaussianBlur(value))
        self.lbShowImage.setPixmap(ImageQt.toqpixmap(self.blurImage))
        
    # 缩放或者扩大图像到屏幕30%
    def getResizeImage(self,img):
        width,height = img.size
        newWidth = int(width*0.3)
        newHeight = int(height*0.3)
        return img.resize((newWidth,newHeight))

if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()