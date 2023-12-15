# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QTime, QTimer, QDateTime
from PySide6.QtGui import QFont, QStandardItemModel, QStandardItem

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from form_ui import Ui_Widget


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.lcdNumber.display(9)
        self.ui.pushButton.setStyleSheet("background-color: #9400D3;")
        
        sheet = "background:transparent;color:#b6e02a;"
        self.ui.lcdNumber_2.setStyleSheet(sheet)

        self.ui.lcdNumber_2.setDigitCount(20)
        self.timer = QTimer()
        self.timer.timeout.connect(self.updatetime)
        self.timer.start(1000)

        model = QStandardItemModel(300, 9)  # 5 rows and 3 columns

        # 设置模型的列名
        model.setHorizontalHeaderLabels(
            [
                "井号",
                "Time",
                "Distance",
                "Distance1",
                "Distance2",
                "valu",
                "amp",
                "temp",
                "electricity",
            ]
        )
        # 创建一个表格视图并使用模型
        self.ui.tableView.setModel(model)

    def red(self):
        a = self.ui.lcdNumber.intValue()
        a -= 1
        print(a)
        self.ui.lcdNumber.display(a)

    def add(self):
        a = self.ui.lcdNumber.intValue()
        a += 1
        print(a)
        self.ui.lcdNumber.display(a)

    def updatetime(self):
        self.time = QDateTime.currentDateTime()
        print(self.time.toString("yyyy-MM-dd hh:mm:ss"))
        self.ui.lcdNumber_2.display(self.time.toString("yyyy-MM-dd hh:mm:ss"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
