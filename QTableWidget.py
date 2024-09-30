from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, \
    QPushButton, QLineEdit, QHBoxLayout
from faker import Faker
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Qt


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.searchItem = []
        self.fake = Faker(locale='zh_CN')
        self.myIcon = QIcon("dragon_ball_icon.ico")
        self.setWindowIcon(self.myIcon)
        self.resize(800, 600)
        self.data = [[self.fake.name(), self.fake.address(), self.fake.ascii_free_email()] for _ in range(80)]
        self.table = QTableWidget()
        self.table.setRowCount(self.data.__len__())
        self.table.setColumnCount(3)

        self.getSelected = QAction("获取选中")
        self.table.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.table.addAction(self.getSelected)

        # 添加一个按钮
        self.btn = QPushButton("输出")

        # 添加一个搜索栏布局
        self.searchLayout =QHBoxLayout()
        self.searchLineEdit = QLineEdit()
        self.searchLineEdit.setPlaceholderText("请输入搜索内容")
        self.searchBtn = QPushButton("搜索")
        self.searchLayout.addWidget(self.searchLineEdit)
        self.searchLayout.addWidget(self.searchBtn)

        # 设置表头
        self.table.setHorizontalHeaderLabels(["姓名", "地址", "邮箱"])
        # 设置表水平方向自动拉伸，一般用这个
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # 设置表水平方向根据内容自适应，缺点是不能拉伸最大
        # self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        # 开启排序
        self.table.setSortingEnabled(True)

        for rowIndex, rowData in enumerate(self.data):
            for colIndex, colData in enumerate(rowData):
                self.table.setItem(rowIndex, colIndex, QTableWidgetItem(colData))

        # 删除第0行0列的数据
        # self.table.takeItem(0, 0)

        # 合并单元格，合并第0行第0列到第1行第1列
        # self.table.setSpan(0, 0, 1, 2)

        # 修改第0行第0列的数据
        # self.table.item(0, 0).setText("我是修改的666")
        # 设置第1行第1列的背景颜色
        # self.table.item(1,1).setBackground(Qt.GlobalColor.red)
        # 设置第1行第1列的前景颜色
        # self.table.item(0,0).setForeground(Qt.GlobalColor.red)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.searchLayout)
        self.mainLayout.addWidget(self.table)
        self.mainLayout.addWidget(self.btn)
        self.setLayout(self.mainLayout)
        self.bind()

    def bind(self):
        # 点击某个单元格事件，下面两种方式都可以
        # self.table.cellClicked.connect(lambda row, col: print(f"点击了第{row}行，第{col}列"))
        self.table.itemClicked.connect(lambda item: print(f"点击了第{item.row()}行，第{item.column()}列"))

        # 绑定按钮事件
        self.btn.clicked.connect(self.outputSelect)

        # 绑定搜索按钮事件
        self.searchBtn.clicked.connect(self.search)

        # 绑定右键菜单事件
        self.getSelected.triggered.connect(self.outputSelect)

    def outputSelect(self):
        # 获取选中的单元格
        items = self.table.selectedItems()
        for item in items:
            print(f"第{item.row()}行，第{item.column()}列的数据是：{item.text()}")

    def search(self):
        if self.searchItem:
            for item in self.searchItem:
                item.setBackground(Qt.GlobalColor.white)
            self.searchItem.clear()
        searchContent = self.searchLineEdit.text()
        result = self.table.findItems(searchContent, Qt.MatchFlag.MatchContains)
        for item in result:
            item.setBackground(Qt.GlobalColor.red)
            self.searchItem.append(item)
        # 滚动到搜索到的第一个结果，PositionAtTop表示滚动到顶部
        self.table.scrollToItem(result[0], QTableWidget.ScrollHint.PositionAtTop)
if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()
