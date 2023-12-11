# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

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
        self.ui.lcdNumber.display(100)
        self.ui.pushButton.setStyleSheet(u"background-color: #9400D3;")

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
