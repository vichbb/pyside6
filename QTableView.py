from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableView, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem

from faker import Faker


# mvc模式

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.fake = Faker(locale='zh_CN')
        self.data = [[self.fake.name(), self.fake.phone_number(), self.fake.address()] for _ in range(80)]

        # 创建模型(存放数据)
        self.model = QStandardItemModel()
        for indexRow, row in enumerate(self.data):
            for indexCol, col in enumerate(row):
                self.model.setItem(indexRow, indexCol, QStandardItem(col))

        # 创建视图(展示数据)
        self.tableView = QTableView()
        # 设置不准编辑
        self.tableView.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
        # 设置选择就是选中整行
        self.tableView.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        # 表头自适应宽度
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableView.setModel(self.model)

        # 设置排序
        self.tableView.setSortingEnabled(True)

        self.tableView2 = QTableView()
        self.tableView2.setModel(self.model)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.tableView)
        self.mainLayout.addWidget(self.tableView2)
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()
