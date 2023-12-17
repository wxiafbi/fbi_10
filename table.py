import time
from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton
class TextEdit(QWidget):
    def __init__(self):
        super(TextEdit, self).__init__()
        self.setWindowTitle("QTextEdit")
        self.setGeometry(300, 300, 500, 300)
        self.UI()
    def UI(self):
        self.tedit = QTextEdit(self)
        self.tedit.setGeometry(10, 10, 200, 100)
        self.tedit.setText("公众号：测个der")
        self.btn = QPushButton("清空tedit", self)
        self.btn.clicked.connect(self.tedit_clear)
        self.btn.setGeometry(220, 10, 70, 30)
        self.tedit_1 = QTextEdit(self)
        self.tedit_1.setPlaceholderText("这里展示微信号")  # clear无法清除，提示作用
        self.tedit_1.setGeometry(10, 120, 200, 100)
        self.btn_1 = QPushButton("插入tedit_1", self)
        self.btn_1.clicked.connect(self.tedit_1_insert)
        self.btn_1.setGeometry(220, 120, 70, 30)
        self.show()
    def tedit_clear(self):
        self.tedit.clear()  # 清除文本
        time.sleep(1)
        self.tedit.append("我是清安")     # 添加文本
    def tedit_1_insert(self):
        self.tedit_1.setFontPointSize(20)   # 设置文本大小
        self.tedit_1.setFontFamily("华文隶书")  # 设置字体
        self.tedit_1.insertPlainText("V: qing_an_an")   # 插入纯文本
if __name__ == '__main__':
    app = QApplication([])
    edit = TextEdit()
    app.exec()