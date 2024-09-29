from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget,QListWidgetItem
from faker import Faker
from PySide6.QtCore import Qt
import random

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.fake = Faker(locale="zh_CN")
        self.listWidget = QListWidget()
        # for _ in range(10):
        #     self.listWidget.addItem(self.fake.name())

        # for _ in range(10):
        #     item = QListWidgetItem(self.fake.name())
        #     self.listWidget.addItem(item)

        self.listWidget.addItems([self.fake.name() for _ in range(20)])

        # 插入一个数字
        self.listWidget.insertItem(0, QListWidgetItem("000"))

        # 插入一串数字
        self.listWidget.insertItems(2, ["123", "456", "789"])

        # 删除:removeItemWidget 没有用，用takeItem
        # self.listWidget.removeItemWidget(self.listWidget.item(0))
        self.listWidget.takeItem(0)


        # 修改一个元素
        self.listWidget.item(1).setText("修改后的元素")

        # 查找一个元素
        self.listWidget.insertItem(5, QListWidgetItem("张三"))
        item = self.listWidget.findItems("张", Qt.MatchFlag.MatchContains)
        for e in item:
            print(e.text())



        # 遍历listWidget
        # for i in range(self.listWidget.count()):
        #     print(f'第{i}个元素是：{self.listWidget.item(i).text()}')


        # 清空listWidget
        self.listWidget.clear()

        # 添加20个随机数
        self.listWidget.addItems([str(random.randint(0,100)) for _ in range(20)])

        self.listWidget.item(3).setText("900")

        # 对列表进行排序,按照第一位数字的大小进行排序
        self.listWidget.sortItems(Qt.SortOrder.AscendingOrder)



        # 给窗体增加上下文菜单
        self.sayHello = QAction("你好", self)
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.addAction(self.sayHello)


        # 给控件增加上下文菜单:输出当前选中的元素
        self.outputCurrentSelectedAction = QAction("输出当前选中的元素", self)
        self.listWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.listWidget.addAction(self.outputCurrentSelectedAction)

        # 给控件增加上下文菜单:删除当前选中的元素
        self.removeCurrentSelectedAction = QAction("删除当前选中的元素", self)
        self.listWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.listWidget.addAction(self.removeCurrentSelectedAction)

        # 将第一个元素设置为可以选中的元素
        self.listWidget.item(0).setFlags(self.listWidget.item(0).flags() | Qt.ItemFlag.ItemIsUserCheckable)
        self.listWidget.item(0).setCheckState(Qt.CheckState.Checked)



        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.listWidget)
        self.setLayout(self.mainLayout)

        self.bind()

    def bind(self):
        self.listWidget.currentItemChanged.connect(self.listChanged)
        self.listWidget.itemChanged.connect(lambda item: print(self.listWidget.currentItem().checkState()))

        # 绑定上下文菜单
        self.sayHello.triggered.connect(lambda: print("你好"))
        self.outputCurrentSelectedAction.triggered.connect(self.outputCurrentSelected)
        self.removeCurrentSelectedAction.triggered.connect(self.removeCurrentSelected)

    def listChanged(self, item, previous):
        if item:
            print(f'当前选则的元素是：{item.text()}')
        # print(f'当前选中的元素是：{item.text()}, 上一个选中的元素是：{previous.text()}')

    def outputCurrentSelected(self):
        print(f'outputCurrentSelected当前选中的元素是：{self.listWidget.currentItem().text()}')

    def removeCurrentSelected(self):
        self.listWidget.takeItem(self.listWidget.currentRow())
if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()