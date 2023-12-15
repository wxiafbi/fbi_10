import sys
from PySide6 import QtWidgets, QtGui
import pandas as pd

class App(QtWidgets.QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.window = Window()
        self.exit()

    def exit(self):
        self.exit_loop = True

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建表格
        self.table_view = QtWidgets.QTableView()
        # 读取Excel数据
        data = pd.read_excel('实时数据.xlsx')
        # 创建模型
        model = QtGui.QStandardItemModel(data.shape[0], data.shape[1])
        for index, row in data.iterrows():
            for col, value in row.items():
                model.setData(model.index(index, col), str(value))
        self.table_view.setModel(model)
        # 设置表格显示的列数
        self.table_view.setColumnCount(data.shape[1])
        # 设置表格的显示样式
        self.table_view.setAlternatingRowColors(True)
        self.table_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # 将表格添加到布局中
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.table_view)
        # 显示窗口
        self.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())