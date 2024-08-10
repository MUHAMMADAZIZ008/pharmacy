from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from Line_Edit import PhoneLineEdit

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # 'PhoneLineEdit' ni to'g'ri yaratish
        self.line_edit1 = PhoneLineEdit("Id: ")
        self.layout.addWidget(self.line_edit1)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Example')
        self.show()

if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    app.exec_()
