import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QMainWindow, QPushButton


class MyAPP(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PyQt5")
        self.move(300, 300)
        self.resize(400, 200)

        btn = QPushButton("button", self)

        layout = QHBoxLayout()
        layout.addWidget(btn)
        self.setLayout(layout)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyAPP()
    sys.exit(app.exec_())
