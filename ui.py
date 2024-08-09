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
    QTableView,
    QHeaderView
)
from PyQt5.QtGui import QIcon, QPixmap, QStandardItem, QStandardItemModel
from PyQt5.QtCore import Qt

from classes import *


class mainPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.showMaximized()
        self.setWindowTitle("Main Page")
        self.v_box = QVBoxLayout()
        self.user_btn = Button("Enter as a user")
        self.admin_btn = Button("Enter as a admin")
        self.user_btn.clicked.connect(self.enter_user_page)
        self.admin_btn.clicked.connect(self.enter_admin_page)

        self.v_box.addWidget(self.user_btn, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.admin_btn, 0, Qt.AlignCenter)

        self.setLayout(self.v_box)
        self.show()

    def enter_user_page(self):
        self.open_user_page = UserLogin()
        self.close()
    def enter_admin_page(self):
        self.open_admin_page = AdminLogin()
        self.close()




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


        self.title_right = QLabel("Najot Pharmacy")
        self.login_input = Edit("Enter a your login...")
        self.password_input = Edit("Enter a your password...")
        self.enter_btn = Button("Enter")
        self.enter_btn.clicked.connect(self.chage_user_page)
        self.registr_btn = Button("Registration")





        #add right
        self.right_box.addStretch(100)
        self.right_box.addWidget(self.title_right, 0, Qt.AlignCenter)
        self.right_box.addStretch(50)
        self.right_box.addWidget(self.login_input, 0, Qt.AlignCenter)
        self.right_box.addStretch(20)
        self.right_box.addWidget(self.password_input, 0, Qt.AlignCenter)

        self.right_box.addStretch(20)
        self.right_box.addWidget(self.enter_btn, 0, Qt.AlignCenter)
        self.right_box.addStretch(20)
        self.right_box.addWidget(self.registr_btn, 0, Qt.AlignCenter)
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
    
    def chage_user_page(self):
        pass
        # self._user_page = ShowUsersPage()
        # self.close()



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
            
        self.title_right = QLabel("Najot Pharmacy")
        self.login_input = Edit("Enter a your login...")
        self.password_input = Edit("Enter a your password...")
        self.enter_btn = Button("Enter")
        self.registr_btn = Button("Registration")





            #add right
        self.right_box.addStretch(100)
        self.right_box.addWidget(self.title_right, 0, Qt.AlignCenter)
        self.right_box.addStretch(50)
        self.right_box.addWidget(self.login_input, 0, Qt.AlignCenter)
        self.right_box.addStretch(20)
        self.right_box.addWidget(self.password_input, 0, Qt.AlignCenter)

        self.right_box.addStretch(20)
        self.right_box.addWidget(self.enter_btn, 0, Qt.AlignCenter)
        self.right_box.addStretch(20)
        self.right_box.addWidget(self.registr_btn, 0, Qt.AlignCenter)
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
        self.enter_btn.setFixedSize(245, 60)

        self.registr_btn.setFixedSize(245, 60)




app = QApplication([])
login_page = mainPage()
app.exec_()