from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableView, QHeaderView
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel
from PySide6.QtCore import Qt, QSortFilterProxyModel


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSqlQueryModel")
        self.resize(800, 600)

        # 和数据库建立连接
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("./test.db")
        if not self.db.open():
            raise Exception("数据库连接失败")

        # 创建一个QSqlQueryModel对象，只读的
        # self.model = QSqlQueryModel()
        # self.model.setQuery("select * from user")

        # 创建一个QSqlQueryModel对象，可读写的
        self.model = QSqlTableModel()
        self.model.setTable("user")
        self.model.select()

        # 创建一个QSortFilterProxyModel对象，代理类
        self.agentModel = QSortFilterProxyModel()
        self.agentModel.setSourceModel(self.model)

        # 修改表头
        header = ["姓名", "地址", "邮箱"]
        for index, head in enumerate(header):
            self.agentModel.setHeaderData(index, Qt.Orientation.Horizontal, head)



        # 创建一个QTableView对象
        self.table = QTableView()

        # 设置表头自动适应宽度
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setModel(self.agentModel)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.table)
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    app.exec()
