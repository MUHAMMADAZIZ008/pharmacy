#Bismillah
from PyQt5.QtWidgets import(
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QSizePolicy
)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

from classes import *

class LoginPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Login Page")
        self.setWindowIcon(QIcon("login_icon.png"))
        self.showMaximized()
        self.UIinit()
        self.show()
    
    def UIinit(self):
        self.main_box = QHBoxLayout()
        self.left_box = QHBoxLayout()
        self.right_box = QVBoxLayout()
        self.box_btn = QHBoxLayout()
        self.input_box = QVBoxLayout()

        self.title_right_box = QLabel("Najot Pharmacy")
        self.login_input = Edit("Enter a your login...")
        self.password_input = Edit("Enter a your password...")
        self.user_btn = Bottom("Login as a user")
        self.admin_btn = Bottom("Login as a admin")

        self.box_btn.addWidget(self.user_btn)
        self.box_btn.addWidget(self.admin_btn)

        #left
        pixmap = QPixmap('Farmacia1.png')

        # scaled_pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label = QLabel()
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.resize(200, 200)



        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.left_box.addWidget(label, alignment=Qt.AlignCenter)
        #add right
        self.right_box.addSpacing(100)
        self.input_box.addWidget(self.title_right_box, alignment=Qt.AlignCenter)
        self.input_box.addSpacing(50)
        self.input_box.addWidget(self.login_input, alignment=Qt.AlignCenter)
        self.input_box.addSpacing(10)
        self.input_box.addWidget(self.password_input, alignment=Qt.AlignCenter)

        self.right_box.addLayout(self.input_box)
        self.right_box.addSpacing(10)
        self.right_box.addLayout(self.box_btn)
        self.right_box.addSpacing(300)

        # self.main_box.addLayout(self.left_box, stretch=1)
        self.main_box.addLayout(self.right_box, stretch=1)


        #add all
        self.setLayout(self.main_box)

        #stle
        self.setStyleSheet("""
            background-color: #fff;
        """)
        self.login_input.setFixedSize(500, 50)
        self.password_input.setFixedSize(500, 50)
        self.title_right_box.setStyleSheet("""
            font-size: 50px;
            font-family: sans-serif;
            color: #211C6A;
            font-weight: 600;

        """)


app = QApplication([])
login_page = LoginPage()
app.exec_()