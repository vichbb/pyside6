from PySide6.QtWidgets import QApplication, QWidget,QMainWindow, QLabel, QVBoxLayout
from Ui_trans import Ui_Form


# 方法2
class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 用于存储数据类型的字典
        self.lengthVar={'米':100,'千米':100000,'厘米':1,'分米':10}
        self.weightVar={'克':1,'千克':1000,'斤':500}  

        self.typeDict = {'长度':self.lengthVar,'重量':self.weightVar}
        
        self.dataTypeComboBox.addItems(self.typeDict.keys())
        self.oneInputComboBox.addItems(self.lengthVar.keys())
        self.twoInputComboBox.addItems(self.lengthVar.keys())
        self.bind()
        
    def bind(self):
        self.dataTypeComboBox.currentTextChanged.connect(self.typeChanged)
        self.calcBtn.clicked.connect(self.calc)
    
    def calc(self):
        bigType = self.dataTypeComboBox.currentText()
        # 获取第一个输入框的值
        value = self.oneInputEditLine.text()
        if value == '':
            return
        currentType = self.oneInputComboBox.currentText()
        transType = self.twoInputComboBox.currentText()
        
        # 把当前值转为最小单位
        standardization = float(value) * self.typeDict[bigType][currentType]
        
        result = standardization / self.typeDict[bigType][transType]
        
        self.originDataLabel.setText(f'{value} {currentType} = ')
        self.transDataLabel.setText(f'{result} {transType}')
        
        self.twoInputEditLine.setText(str(result))

    def typeChanged(self,text):
        self.oneInputComboBox.clear()
        self.twoInputComboBox.clear()
        
        self.oneInputComboBox.addItems(self.typeDict[text].keys())
        self.twoInputComboBox.addItems(self.typeDict[text].keys())
    
if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()
