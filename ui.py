#Bismillah
from PyQt5.QtWidgets import(
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLayout,
    QLabel,
    QTableView,
    QHeaderView,
)
from PyQt5.QtGui import QIcon, QPixmap, QStandardItem, QStandardItemModel, QPainter
from PyQt5.QtCore import Qt

from core import *

from classes import *

class mainPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.showMaximized()
        self.setWindowIcon(QIcon("logo.png"))
        self.setWindowTitle("Main Page")
        self.v_box = QVBoxLayout()
        self.user_btn = Button("Enter as a user")
        self.admin_btn = Button("Enter as a admin")

        self.main_title = QLabel("Najot Pharmacy")

        self.user_btn.clicked.connect(self.enter_user_page)
        self.admin_btn.clicked.connect(self.enter_admin_page)

        self.v_box.addWidget(self.main_title, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.user_btn, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.admin_btn, 0, Qt.AlignCenter)

        self.setLayout(self.v_box)
        self.show()

        #style
        self.paintEvent(1)


        self.main_title.setStyleSheet("""
            font-size: 60px;
            font-family: sans-serif;
            color: #211C6A;
            font-weight: 600;
        """)
    def enter_user_page(self):
        self.open_user_page = UserLogin()
        self.close()

    def enter_admin_page(self):
        self.open_admin_page = AdminLogin()
        self.close()
    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("main_bg2.jpg") 
        painter.drawPixmap(self.rect(), pixmap) 
        painter.end()

class UserLogin(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.showMaximized()
        self.setWindowTitle("Login Page")
        self.setWindowIcon(QIcon("logo.png"))
        self.core = Database()
        self.UIinit()
        self.show()
    
    def UIinit(self):
        self.main_box = QHBoxLayout()
        self.right_box = QVBoxLayout()

        self.title_right = QLabel("Najot Pharmacy")
        self.login_input = Edit("Enter a your login...")
        self.password_input = Edit("Enter a your password...")
        self.info_label = QLabel()
        self.enter_btn = Button("Enter")
        self.enter_btn.clicked.connect(self.Enter_user_page)
        self.registr_btn = Button("Registration")
        self.registr_btn.clicked.connect(self.user_register)

        #add right
        self.right_box.addStretch(100)
        self.right_box.addWidget(self.title_right, 0, Qt.AlignCenter)
        self.right_box.addStretch(50)
        self.right_box.addWidget(self.login_input, 0, Qt.AlignCenter)
        self.right_box.addStretch(20)
        self.right_box.addWidget(self.password_input, 0, Qt.AlignCenter)
        self.right_box.addStretch(10)
        self.right_box.addWidget(self.info_label, 0, Qt.AlignCenter)

        self.right_box.addStretch(20)
        self.right_box.addWidget(self.enter_btn, 0, Qt.AlignCenter)
        self.right_box.addStretch(20)
        self.right_box.addWidget(self.registr_btn, 0, Qt.AlignCenter)
        self.right_box.addStretch(100)

        self.main_box.addLayout(self.right_box)

        #add all
        self.setLayout(self.main_box)

        #style
        self.login_input.setFixedSize(500, 50)
        self.password_input.setFixedSize(500, 50)
        self.title_right.setStyleSheet("""
            font-size: 60px;
            font-family: sans-serif;
            color: #211C6A;
            font-weight: 600;
        """)
        self.info_label.setStyleSheet("""
            color: red;
            font-size: 30px;
        """)

    
    def Enter_user_page(self):
        items = self.core.Get_all_medicine_items()
        self.close()
        self.admin_page = Medicine_buy(items)

    def user_register(self):
        self.close()
        self.registration = RegistrationPage()

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

class RegistrationPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registration")
        self.showMaximized()
        self.setStyleSheet("""
            font-size: 30px
        """)

        self.initUI()
    
    def initUI(self):
        self.v_box = QVBoxLayout()
        self.title = QLabel("Registration")
        self.username_input = Edit("Username")
        self.password_input = Edit("Password")
        self.phone_number_input = Edit()
        self.warning_user = QLabel()
        self.warning_number = QLabel()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.info_label = QLabel()

        self.save_btn = Button("Save user")
        self.save_btn.clicked.connect(self.create_user)

        self.v_box.addStretch(50)
        self.v_box.addWidget(self.title, 0, Qt.AlignCenter)
        self.v_box.addStretch(30)
        self.v_box.addWidget(self.username_input, 0, Qt.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.password_input, 0, Qt.AlignCenter)

        self.v_box.addStretch(5)
        self.v_box.addWidget(self.info_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.phone_number_input, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.warning_number, 0, Qt.AlignCenter)
        self.v_box.addStretch(3)
        self.v_box.addWidget(self.save_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(40)

        self.style()

        self.setLayout(self.v_box)
        self.show()

    def style(self):
        self.username_input.setFixedSize(450, 50)
        self.password_input.setFixedSize(450, 50)
        self.phone_number_input.setFixedSize(450, 50)
        # self.phone_number_input.setText("+998 ")
        self.phone_number_input.setPlaceholderText("+998-90-123-45-67")

        self.title.setStyleSheet("""
            font-size: 60px;
            font-weight: 600;
            color: #FF8225;
        """)
        self.warning_number.setStyleSheet("""
            font-size: 30px;
            color: red;
        """)
        self.info_label.setStyleSheet("""
            font-size: 30px;
            color: red;
        """)


    def create_user(self):
        self.core = Database()
        username = self.username_input.text()
        password = self.password_input.text()
        phone_number = self.phone_number_input.text()
        self.info_label.clear()
        if not (username and password):
            self.info_label.setText("Empty login or password!!!")
            return
        if not phone_number:
            self.warning_number.setText("Empty phone number!!!")
            return
        if not (phone_number[1:].isdigit() and phone_number[0] == "+" and len(phone_number) == 12):
            self.warning_number.setText("Enter the number correctly!!!")
            return

        user = {
            'username' : username,
            'password' : password,
            'phone_number': phone_number
        } 
        err = self.core.insert_user(user)
        if err:
            self.info_label.setText("Incorrect login or password")
        
class Medicine_buy(QWidget):
    def __init__(self, items: list) -> None:
        self.medicine_items = items
        print(self.medicine_items)
        super().__init__()
        self.showMaximized()
        self.setWindowTitle("Najot Pharmacy")
        self.setWindowIcon(QIcon("login_icon.png"))
        self.show()

        self.initUI()

    def initUI(self):

        self.vbox = QVBoxLayout()

        self.hbox = QHBoxLayout()
        self.hbox2 = QHBoxLayout()

        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Id")
        self.line_edit.setFixedWidth(130)
        self.hbox.addWidget(self.line_edit)

        self.update_button = QPushButton("Updete User", self)
        self.update_button.setFixedWidth(130)
        self.delete_button = QPushButton("Delete User", self)
        self.delete_button.setFixedWidth(130)  
        self.exit = QPushButton("Exit", self)
        self.exit.setFixedWidth(130)

        self.users_infos = QTableView(self)
        
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Product", "Produced time", "End time", "Muddati", "Narxi"])

        self.add_data_to_model(self.medicine_items)

        self.users_infos.setModel(self.model)

        self.users_infos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.hbox2.addWidget(self.users_infos)

        self.hbox.addStretch()
        self.hbox.addWidget(self.update_button)
        self.hbox.addWidget(self.delete_button)
        self.hbox.addWidget(self.exit)

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox2)
        self.setLayout(self.vbox)

        self.users_infos.clicked.connect(self.on_cell_clicked)
        

    def on_cell_clicked(self, index):
        if index.column() == 0: 
            data = self.model.itemFromIndex(index).text()
            self.line_edit.setText(data)

    def add_data_to_model(self, data):
        if self.model.rowCount() == 0:
            for row in data:
                items = [QStandardItem(str(field)) for field in row]
                self.model.appendRow(items[1:-1])
        else:
            self.model.removeRows(0, self.model.rowCount())
            self.line_edit.clear()
            for row in data:
                items = [QStandardItem(str(field)) for field in row]
                self.model.appendRow(items[1:-1])

app = QApplication([])
login_page = mainPage()
app.exec_()