from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QSpinBox, QSlider, QComboBox, QPushButton,QLabel
from PySide6.QtCore import Qt
from qt_material import apply_stylesheet

# https://github.com/UN-GCPDS/qt-material

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("美化")
        self.le = QLineEdit()
        self.btn = QPushButton("按钮")
        self.lb = QLabel("标签")
        self.spinBox = QSpinBox()
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.combo = QComboBox()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.le)
        self.mainLayout.addWidget(self.btn)
        self.mainLayout.addWidget(self.lb)
        self.mainLayout.addWidget(self.spinBox)
        self.mainLayout.addWidget(self.slider)
        self.mainLayout.addWidget(self.combo)
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication([])
    apply_stylesheet(app, theme='dark_teal.xml')
    myWin = MyWindow()
    myWin.show()
    app.exec()
