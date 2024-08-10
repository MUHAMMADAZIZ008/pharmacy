#Bismillah
from PyQt5.QtWidgets import(
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QStyledItemDelegate,
    QLabel,
    QTableView,
    QHeaderView,
    QMessageBox
)
from PyQt5.QtGui import (
    QIcon, 
    QPixmap, 
    QStandardItem, 
    QStandardItemModel, 
    QPainter, 
    QColor, 
    QBrush, 
    QIcon
    )

from PyQt5.QtCore import Qt, QEvent
from Line_Edit import PhoneLineEdit
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
        self.core = Database()
        self.UIinit()
        self.show()
        
    def UIinit(self):
        self.main_box = QHBoxLayout()
        self.right_box = QVBoxLayout()
            
        self.title_right = QLabel("Login to the admin page")
        self.login_input = Edit("Enter a your login...")
        self.password_input = Edit("Enter a your password...")
        self.info_lable = QLabel()
        self.enter_btn = Button("Enter")
        self.enter_btn.clicked.connect(self.enter_admin_page)
        self.back_btn = Button("🔙")
        self.back_btn.clicked.connect(self.beck_main)



        #add right
        self.right_box.addStretch(100)
        self.right_box.addWidget(self.title_right, 0, Qt.AlignCenter)
        self.right_box.addStretch(50)
        self.right_box.addWidget(self.login_input, 0, Qt.AlignCenter)
        self.right_box.addStretch(20)
        self.right_box.addWidget(self.password_input, 0, Qt.AlignCenter)

        self.right_box.addStretch(10)
        self.right_box.addWidget(self.info_lable, 0, Qt.AlignCenter)
        self.right_box.addStretch(10)
        self.right_box.addWidget(self.enter_btn, 0, Qt.AlignCenter)
        self.right_box.addStretch(20)
        self.right_box.addWidget(self.back_btn, 0, Qt.AlignCenter)
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
        self.info_lable.setStyleSheet("""
            color: red;
            font-size: 30px;
        """)


    def enter_admin_page(self):
        items = self.core.Get_all_medicine_items()
        login = self.login_input.text()
        password = self.password_input.text()
        users = {
            "login" : login,
            "password" : password
        }
        _id = self.core.get_admin_data(users)
        self.info_lable.clear()
        # if not (login and password):
        #     self.info_lable.setText("Empty login or password!!!")
        #     return
        # print(_id)
        # if not _id:
        #     self.info_lable.setText("Login or password is error!!!")
        #     return
        self.close()
        self.open_admin_page = AdminPage(items)     

    def beck_main(self):
        self.close()
        self.open_main_page = mainPage()

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
        self.phone_number_input = PhoneLineEdit("+998")
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
        # self.phone_number_input.setPlaceholderText("+998-90-123-45-67")

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
        print(phone_number)
        self.info_label.clear()
        if not (username and password):
            self.info_label.setText("Empty login or password!!!")
            return
        if not phone_number:
            self.warning_number.setText("Empty phone number!!!")
            return
        if not (phone_number[1:].isdigit() and phone_number[0] == "+" and len(phone_number) == 13):
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


class ColorfulDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter, option, index):
        if not painter:
            return

        if index.column() == 0: 
            painter.fillRect(option.rect, QBrush(QColor("#E0FFFF")))
        elif index.column() == 1:
            painter.fillRect(option.rect, QBrush(QColor("#FFFFE0")))
        elif index.column() == 2:
            painter.fillRect(option.rect, QBrush(QColor("green")))
        
        super().paint(painter, option, index)


class Medicine_buy(QWidget):
    def __init__(self, items: list) -> None:
        super().__init__()
        self.medicine_items = items
        self.showMaximized()
        self.setWindowTitle("Najot Pharmacy")
        self.setWindowIcon(QIcon("login_icon.png"))

        self.setStyleSheet("""
            QHBoxLayout{
                background: yellow;
            }
            QLineEdit{
                background: #F5F5F5;
                font-size: 25px;
                border-radius: 10px;
                padding: 5px;
                padding-left: 10px
            }
            QPushButton{
                background-color: #4B0082;
                color: white;
                font-size: 25px;
                border-radius: 10px;
                padding: 5px;
                padding-left: 10px
            }
            QTableView {
                border: 1px solid #4B0082;
                alternate-background-color: #F0F0F0;
                gridline-color: #4B0082;
            }
            QHeaderView::section {
                background-color: #4B0082;
                color: white;
                font-size: 15px;
                padding: 5px;
                border: 1px solid #4B0082;
            }
            QTableView::item {
                padding: 5px;
            }""")

        self.initUI()

    def initUI(self):
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.hbox2 = QHBoxLayout()

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Search")
        self.line_edit.setFixedSize(400, 50)
        self.hbox.addStretch(10)
        self.hbox.addWidget(self.line_edit)
        self.hbox.addStretch(10)

        self.card_btn = QPushButton("Korzinka 🧺")
        self.card_btn.setFixedSize(150, 50)
        self.exit = QPushButton("Chiqish")
        self.exit.setFixedSize(150, 50)

        self.users_infos = QTableView(self)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Product", "Produced time", "End time", "Muddati", "Narxi"])

        self.add_data_to_model(self.medicine_items)

        self.users_infos.setModel(self.model)

        self.users_infos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.hbox2.addWidget(self.users_infos)

        colorful_delegate = ColorfulDelegate(self)

        self.users_infos.setItemDelegate(colorful_delegate)

        self.hbox.addStretch()
        self.hbox.addWidget(self.card_btn)
        self.hbox.addWidget(self.exit)

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox2)
        self.setLayout(self.vbox)

        self.line_edit.textChanged.connect(self.search_items)
        self.users_infos.clicked.connect(self.on_cell_clicked)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(255, 255, 200))

    def search_items(self):
        search_term = self.line_edit.text().lower()
        for row in range(self.model.rowCount()):
            item = self.model.item(row, 0)
            if search_term in item.text().lower():
                self.users_infos.setRowHidden(row, False)
            else:
                self.users_infos.setRowHidden(row, True)

        self.card_btn.setStyleSheet("""
            background-color: #03C988;
        """)

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



class AdminPage(QWidget):
    def __init__(self, items: list) -> None:
        super().__init__()
        self.medicine_items = items
        print(self.medicine_items)
        self.showMaximized()
        self.setWindowTitle("Admin Page")
        self.setWindowIcon(QIcon("login_icon.png"))

        self.setStyleSheet("""
            QHBoxLayout{
                background: yellow;
            }
            QLineEdit{
                background: #F5F5F5;
                font-size: 25px;
                border-radius: 10px;
                padding: 5px;
                padding-left: 10px
            }
            QPushButton{
                background-color: #4B0082;
                color: white;
                font-size: 25px;
                border-radius: 10px;
                padding: 5px;
                padding-left: 10px
            }
            QTableView {
                border: 1px solid #4B0082;
                alternate-background-color: #F0F0F0;
                gridline-color: #4B0082;
            }
            QHeaderView::section {
                background-color: #4B0082;
                color: white;
                font-size: 15px;
                padding: 5px;
                border: 1px solid #4B0082;
            }
            QTableView::item {
                padding: 5px;
            }""")

        self.initUI()

    def initUI(self):
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.main_box = QHBoxLayout()
        self.left_box = QVBoxLayout()

        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("🔍 Search")
        self.line_edit.setFixedSize(400, 50)
        self.hbox.addStretch(10)
        self.hbox.addWidget(self.line_edit)
        self.hbox.addStretch(10)

        self.exit = Button("Exit")
        self.exit.clicked.connect(self.exit_sys)
        self.exit.setFixedSize(150, 50)

        self.madicine_table = QTableView(self)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Product", "Produced time", "End time", "Muddati", "Narxi", "Count"])

        self.add_data_to_model(self.medicine_items)

        self.madicine_table.setModel(self.model)

        self.madicine_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        delegate = ColorfulDelegate(self)
        self.madicine_table.setItemDelegate(delegate)

        #left
        self.update_product = Button("Update")
        self.update_product.clicked.connect(self.update_poduct_database)

        self.delete_product = Button("Delete")
        self.expired_product = Button("Expired")
        self.left_box.addWidget(self.update_product)
        self.left_box.addWidget(self.delete_product)
        self.left_box.addWidget(self.expired_product)

        self.hbox2.addWidget(self.madicine_table, stretch=5)
        self.hbox2.addLayout(self.left_box, stretch=1)
        self.hbox.addStretch()
        self.hbox.addWidget(self.exit)

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox2)
        self.setLayout(self.vbox)

        self.line_edit.textChanged.connect(self.search_items)
        self.madicine_table.clicked.connect(self.on_cell_clicked)
        self.show()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(255, 255, 200))



    def search_items(self):
        search_term = self.line_edit.text().lower()
        for row in range(self.model.rowCount()):
            item = self.model.item(row, 0)
            if search_term in item.text().lower():
                self.madicine_table.setRowHidden(row, False)
            else:
                self.madicine_table.setRowHidden(row, True)

    def on_cell_clicked(self, index):
        if index.column() == 0:
            data = self.model.itemFromIndex(index).text()
            self.line_edit.setText(data)

    def add_data_to_model(self, data):
        if self.model.rowCount() == 0:
            for row in data:
                items = [QStandardItem(str(field)) for field in row]
                self.model.appendRow(items[1:])
        else:
            self.model.removeRows(0, self.model.rowCount())
            self.line_edit.clear()
            for row in data:
                items = [QStandardItem(str(field)) for field in row]
                self.model.appendRow(items[1:])
    
    def update_poduct_database(self):
        for row in range(self.model.rowCount()):
            product_dic = {}
            product = self.model.item(row, 0).text()
            produced_time = self.model.item(row, 1).text()
            end_time = self.model.item(row, 2).text()
            muddati = self.model.item(row, 3).text()
            narxi = self.model.item(row, 4).text()
            product_dic = {
                "name": product,
                "produced_time" : produced_time,
                "end_time" : end_time,
                "expiration_date" : muddati,
                "price" : narxi
            }
            self.core.update_tabele(product_dic)


        QMessageBox.information(self, "Success", "Data updated in the database successfully.")


    def exit_sys(self):
        self.close()


app = QApplication([])
login_page = mainPage()
app.exec_()