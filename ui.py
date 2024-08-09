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
)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QUrl

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

from classes import *


class UserLogin(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.showMaximized()
        self.setWindowTitle("Login Page")
        self.setWindowIcon(QIcon("login_icon.png"))
        self.UIinit()
        self.show()
    
    def UIinit(self):
        self.main_box = QHBoxLayout()
        self.right_box = QVBoxLayout()
        self.box_btn = QHBoxLayout()

        self.title_right = QLabel("Najot Pharmacy")
        self.login_input = Edit("Enter a your login...")
        self.password_input = Edit("Enter a your password...")
        self.user_btn = Botton("Login as a user")
        self.admin_btn = Botton("Login as a admin")

        self.box_btn.addWidget(self.user_btn)
        self.box_btn.addWidget(self.admin_btn)


        #left




        #add right
        self.right_box.addStretch(100)
        self.right_box.addWidget(self.title_right, 0, Qt.AlignCenter)
        self.right_box.addStretch(50)
        self.right_box.addWidget(self.login_input, 0, Qt.AlignCenter)
        self.right_box.addStretch(20)
        self.right_box.addWidget(self.password_input, 0, Qt.AlignCenter)

        self.right_box.addStretch(20)
        self.right_box.addLayout(self.box_btn)
        self.right_box.addStretch(100)

        self.main_box.addLayout(self.right_box)

        #add all
        self.setLayout(self.main_box)

        #stle



        self.login_input.setFixedSize(500, 50)
        self.password_input.setFixedSize(500, 50)
        self.title_right.setStyleSheet("""
            font-size: 60px;
            font-family: sans-serif;
            color: #211C6A;
            font-weight: 600;
        """)
        self.user_btn.setFixedSize(245, 60)

        self.admin_btn.setFixedSize(245, 60)




    class AdminLogin(QWidget):
        def __init__(self) -> None:
            super().__init__()
            self.showMaximized()
            self.setWindowTitle("Login Page")
            self.setWindowIcon(QIcon("login_icon.png"))
            self.UIinit()
            self.show()
        
        def UIinit(self):
            self.main_box = QHBoxLayout()
            self.right_box = QVBoxLayout()
            self.box_btn = QHBoxLayout()

            self.title_right = QLabel("Najot Pharmacy")
            self.login_input = Edit("Enter a your login...")
            self.password_input = Edit("Enter a your password...")
            self.enter_btn = Botton("Enter")
            self.admin_btn = Botton("Login as a admin")

            self.box_btn.addWidget(self.user_btn)
            self.box_btn.addWidget(self.admin_btn)


            #left




            #add right
            self.right_box.addStretch(100)
            self.right_box.addWidget(self.title_right, 0, Qt.AlignCenter)
            self.right_box.addStretch(50)
            self.right_box.addWidget(self.login_input, 0, Qt.AlignCenter)
            self.right_box.addStretch(20)
            self.right_box.addWidget(self.password_input, 0, Qt.AlignCenter)

            self.right_box.addStretch(20)
            self.right_box.addLayout(self.box_btn)
            self.right_box.addStretch(100)

            self.main_box.addLayout(self.right_box)

            #add all
            self.setLayout(self.main_box)

            #stle



            self.login_input.setFixedSize(500, 50)
            self.password_input.setFixedSize(500, 50)
            self.title_right.setStyleSheet("""
                font-size: 60px;
                font-family: sans-serif;
                color: #211C6A;
                font-weight: 600;
            """)
            self.user_btn.setFixedSize(245, 60)

            self.admin_btn.setFixedSize(245, 60)


app = QApplication([])
login_page = UserLogin()
app.exec_()