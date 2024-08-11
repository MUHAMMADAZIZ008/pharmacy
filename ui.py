#Bismillah
from PyQt5.QtWidgets import(
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QStyledItemDelegate,
    QLabel,
    QTableView,
    QListWidget,
    QHeaderView,
    QMessageBox,
    QAbstractItemView,
    QListWidgetItem
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

from PyQt5.QtCore import Qt

from Line_Edit import PhoneLineEdit

from core import *

from classes import *

from datetime import datetime


class mainPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.showMaximized()
        self.setWindowIcon(QIcon("logo.png"))
        self.setWindowTitle("Main Page")
        self.v_box = QVBoxLayout()
        self.box_btn = QHBoxLayout()
        self.user_btn = Button("Enter as a user")
        self.admin_btn = Button("Enter as a admin")

        self.box_btn.addStretch(50)
        self.box_btn.addWidget(self.user_btn)
        self.box_btn.addStretch(20)
        self.box_btn.addWidget(self.admin_btn)
        self.box_btn.addStretch(50)

        self.main_title = QLabel("Najot Pharmacy")

        self.user_btn.clicked.connect(self.enter_user_page)
        self.admin_btn.clicked.connect(self.enter_admin_page)

        self.v_box.addStretch(40)
        self.v_box.addWidget(self.main_title, 0, Qt.AlignCenter)
        self.v_box.addStretch(30)
        self.v_box.addLayout(self.box_btn)
        self.v_box.addStretch(50)

        self.setLayout(self.v_box)
        self.show()

        self.paintEvent(1)


        self.main_title.setStyleSheet("""
            font-size: 65px;
            font-family: sans-serif;
            color: #393E46;
            font-weight: 600;
        """)
        self.user_btn.setFixedSize(300, 70)
        self.admin_btn.setFixedSize(300, 70)
    def enter_user_page(self):
        self.open_user_page = UserLogin()
        self.close()

    def enter_admin_page(self):
        self.open_admin_page = AdminLogin()
        self.close()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("main_bg3.png") 
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

        self.setLayout(self.main_box)

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
        login = self.login_input.text()
        password = self.password_input.text()
        users = {
            "login" : login,
            "password" : password
        }
        _id = self.core.get_user_data(users)
        if not (login and password):
            self.info_label.setText("Empty login or password!!!")
            return
        if not _id:
            self.info_label.setText("Login or password is error!!!")
            return
        self.info_label.clear()
        self.close()
        self.open_admin_page = Medicine_buy(items)   


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
        if not (login and password):
            self.info_lable.setText("Empty login or password!!!")
            return
        print(_id)
        if not _id:
            self.info_lable.setText("Login or password is error!!!")
            return
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
        self.core = Database()

        self.initUI()
    
    def initUI(self):
        self.v_box = QVBoxLayout()
        self.title = QLabel("Registration")
        self.username_input = Edit("Username")
        self.password_input = Edit("Password")
        self.phone_number_input = PhoneLineEdit("+998")
        self.phone_number_input.setInputMask("+999999999999")

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
        username = self.username_input.text()
        password = self.password_input.text()
        phone_number = self.phone_number_input.text()
        self.info_label.clear()
        self.warning_number.clear()
        
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
            'username': username,
            'password': password,
            'phone_number': phone_number
        }
        
        success = self.core.insert_user(user, self.info_label, self.warning_number)
        if success:
            self.open_medicine_buy() 

    def open_medicine_buy(self):
        items = self.core.Get_all_medicine_items()        
        self.medicine_buy_page = Medicine_buy(items)
        self.close()





class ColorfulDelegate(QStyledItemDelegate):
    def __init__(self, parent=None, font_size=14, cell_height=30):
        super().__init__(parent)
        self.font_size = font_size
        self.cell_height = cell_height

    def paint(self, painter, option, index):
        if not painter:
            return
     
        column_colors = {
            0: "#FF8225", 
            1: "#003366",
            2: "#006400",
            3: "#2E8B57",
            4: "#8B0000",
            5: "#5F939A",
            6: "#068FFF"
        }

        
        color = column_colors.get(index.column(), "#FFFFFF")
        painter.fillRect(option.rect, QBrush(QColor(color)))

        painter.setPen(QColor("#FFFFFF"))
        option.font.setPointSize(self.font_size)
        painter.setFont(option.font)


        option.displayAlignment = Qt.AlignCenter


        text = index.data()
        painter.drawText(option.rect, option.displayAlignment, text)



    def set_column_widths(self, table_view, widths):
        for i, width in enumerate(widths):
            table_view.setColumnWidth(i, width)

    def set_row_heights(self, table_view):
        row_count = table_view.model().rowCount()
        for row in range(row_count):
            table_view.setRowHeight(row, self.cell_height)
    

    def apply_delegate(self, table_view):
        table_view.setItemDelegate(self)

        self.set_column_widths(table_view, [120] * table_view.model().columnCount())

        self.set_row_heights(table_view)



class Medicine_buy(QWidget):
    def __init__(self, items: list) -> None:
        super().__init__()
        self.medicine_items = items
        self.cart_items = [] 
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
                font-size: 25px;
                padding: 5px;
                border: 1px solid #4B0082;
            }
            QTableView::item {
                padding: 5px;
            }""")

        self.initUI()

    def initUI(self):
        self.vbox = QVBoxLayout()
        self.navbar_box = QHBoxLayout()
        self.hbox2 = QHBoxLayout()

        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("Search")
        self.search_edit.setFixedSize(400, 50)
        self.navbar_box.addStretch(20)
        self.navbar_box.addWidget(self.search_edit)
        self.navbar_box.addStretch(1)

        self.amount = QLineEdit()
        self.amount.setPlaceholderText("Quantity")
        self.amount.setStyleSheet("font-size: 20px;")
        self.amount.setFixedSize(100, 50)
        self.navbar_box.addWidget(self.amount)

        self.add_btn = QPushButton("Add")
        self.add_btn.setFixedSize(100, 50)
        self.navbar_box.addWidget(self.add_btn)
        self.add_btn.clicked.connect(self.add_to_card)
        self.navbar_box.addStretch(10)



        self.card_btn = QPushButton("Buy")
        self.card_btn.setFixedSize(150, 50)
        self.navbar_box.addWidget(self.card_btn)
        self.card_btn.clicked.connect(self.To_Buy_Medicine)


        self.Korzina_items = QListWidget()
        self.Korzina_items.maximumHeight()
        self.Korzina_items.maximumWidth()
        self.Korzina_items.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Korzina_items.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff) 



        self.exit = QPushButton("Chiqish")
        self.exit.setFixedSize(150, 50)
        self.navbar_box.addWidget(self.exit)
        self.exit.clicked.connect(self.exit_sys)
        self.users_infos = QTableView(self)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Product", "Produced time", "End time", "Muddati", "Narxi"])

        self.add_data_to_model(self.medicine_items)

        self.users_infos.setModel(self.model)

        self.users_infos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.hbox2.addWidget(self.users_infos, 3)
        self.hbox2.addWidget(self.Korzina_items, 1)

        self.users_infos.setEditTriggers(QAbstractItemView.NoEditTriggers)

        colorful_delegate = ColorfulDelegate(self)

        self.users_infos.setItemDelegate(colorful_delegate)


        delegate = ColorfulDelegate(font_size=18, cell_height=60)
        delegate.apply_delegate(self.users_infos)

        self.navbar_box.addStretch()

        self.vbox.addLayout(self.navbar_box)
        self.vbox.addLayout(self.hbox2)
        self.setLayout(self.vbox)

        self.search_edit.textChanged.connect(self.search_items)
        self.users_infos.clicked.connect(self.on_cell_clicked)
        self.show()


    def To_Buy_Medicine(self):
        self.to_buy = Buying_items(items=self.cart_items)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(255, 255, 200))



    def remove_item(self, item):
        row = self.Korzina_items.row(item)
        self.Korzina_items.takeItem(row)
        
        self.cart_items.pop(row)
        
        self.update_summary()



    def search_items(self):
        search_term = self.search_edit.text().lower()
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
            self.search_edit.setText(data)



    def add_to_card(self):
        product_name = self.search_edit.text()
        quantity_text = self.amount.text()

        try:
            quantity = int(quantity_text)
        except ValueError:
            return

        price_text = self.get_product_price(product_name)
        if price_text is None:
            return

        try:
            price = int(price_text)
        except ValueError:
            return

        item_widget = QWidget()
        item_layout = QHBoxLayout()
        label = QLabel(f"{product_name} - {quantity} ta,  {quantity*price} so'm")
        label.setStyleSheet("font-size: 20px;")
        remove_button = QPushButton("Remove")
        remove_button.setFixedSize(100, 30)
        remove_button.setStyleSheet("font-size: 20px;")
        item_layout.addWidget(label)
        item_layout.addWidget(remove_button)
        item_widget.setLayout(item_layout)

        list_item = QListWidgetItem()
        list_item.setSizeHint(item_widget.sizeHint())
        self.Korzina_items.addItem(list_item)
        self.Korzina_items.setItemWidget(list_item, item_widget)

        remove_button.clicked.connect(lambda checked, item=list_item: self.remove_item(item))

        self.cart_items.append({
            'product_name': product_name,
            'quantity': int(quantity_text),
            'price': int(price_text)
        })

        self.update_summary()

        self.search_edit.clear()
        self.amount.clear()

    def update_summary(self):
        all_items_text = ""
        total_amount = 0

        for item in self.cart_items:
            item_text = f"{item['product_name']} - {item['quantity']} ta, {item['price']*item['quantity']} so'm\n"
            all_items_text += item_text
            total_amount += item['price'] * item['quantity']
        
        if not self.cart_items:
            all_items_text = "No items in cart.\n"
        
        summary_text = f"Najot pharmacy\n{all_items_text}Jami: {total_amount} so'm"
        
        print(summary_text)



    def get_product_price(self, product_name):
        for row in range(self.model.rowCount()):
            item = self.model.item(row, 0)
            if item.text() == product_name:
                price_item = self.model.item(row, 4)
                return price_item.text().replace(" so'm", "")
        return None


    def add_data_to_model(self, data):

        if self.model.rowCount() > 0:
            self.model.removeRows(0, self.model.rowCount())
            self.search_edit.clear()

        for row in data:

            items = [QStandardItem(str(field)) for field in row]

            if items:
                price = items[-2]
                price.setText(f"{price.text()} so'm")
                year = items[-3]
                year.setText(f"{year.text()} yil")


            self.model.appendRow(items[1:-1])

    def exit_sys(self):
        self.close()

class Buying_items(QWidget):
    def __init__(self, items: list) -> None:
        super().__init__()
        self.medicine_items = items
        self.total_amount = 0
        self.setFixedSize(700, 800)
        self.setWindowTitle("Buying")
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
                font-size: 25px;
                padding: 5px;
                border: 1px solid #4B0082;
            }
            QTableView::item {
                padding: 5px;
            }""")

        self.initUI()

    def initUI(self):

        self.vbox = QVBoxLayout()
        self.info = QVBoxLayout()
        self.v_pay = QVBoxLayout()

        all_items_text = ""
        for item in self.medicine_items:
            item_text = f"{item['product_name']} - {item['quantity']} ta, {item['price']*item['quantity']} so'm\n"
            all_items_text += item_text
            self.total_amount += item['price'] * item['quantity']

        self.summary_label = QLabel(f"          Najot pharmacy\n{all_items_text}Jami: {self.total_amount} so'm")
        self.summary_label.setStyleSheet("font-size: 20px; padding-left: 20px; background: yellow;")
        
        self.info.addWidget(self.summary_label)
        self.vbox.addLayout(self.info)
        self.vbox.addStretch(1)

        self.carta_info = QLabel("Karta raqamingizni kiriting:")
        self.carta_info.setFixedSize(400, 40)
        self.carta_info.setStyleSheet("font-size: 20px; margin-left: 10px;")
        self.v_pay.addWidget(self.carta_info)

        self.add_carta = QLineEdit()
        self.add_carta.setInputMask("9999 9999 9999 9999")
        self.add_carta.setStyleSheet("background: white; font-size: 20px; padding-left: 10px; margin-left: 10px;")
        self.add_carta.setFixedSize(400, 60)
        self.v_pay.addWidget(self.add_carta)

        self.date_info = QLabel("Amal qilish muddati (MM/YY):")
        self.date_info.setFixedSize(400, 40)
        self.date_info.setStyleSheet("font-size: 20px; margin-left: 10px;")
        self.v_pay.addWidget(self.date_info)

        self.add_date = QLineEdit()
        self.add_date.setInputMask("99/99")
        self.add_date.setStyleSheet("background: white; font-size: 20px; padding-left: 10px; margin-left: 10px;")
        self.add_date.setFixedSize(100, 60)
        self.v_pay.addWidget(self.add_date)

        self.v_pay.addStretch(1)


        self.submit_button = QPushButton('Tasdiqlash')
        self.submit_button.clicked.connect(self.validate_inputs)
        self.v_pay.addWidget(self.submit_button)
        

        self.vbox.addLayout(self.v_pay)


        self.setLayout(self.vbox)
        self.show()


    def validate_inputs(self):

        valid_cards = ['8600', '9860', '2200', '4276', '5312', '4283', '4831']
        carta = self.add_carta.text().replace(" ", "")
        if carta[:4] not in valid_cards or len(carta) != 16:
            QMessageBox.warning(self, "Xatolik", "Karta raqam noto'g'ri, qaytadan kiriting")
            self.add_carta.setFocus()
            return

        date_text = self.add_date.text()
        try:
            month, year = map(int, date_text.split('/'))
            if not (1 <= month <= 12 and 2024 <= 2000 + year <= 2035):
                QMessageBox.warning(self, "Xatolik", "Amal qilish muddati noto'g'ri, qaytadan kiriting")
                self.add_date.setFocus()
                return
        except ValueError:
            QMessageBox.warning(self, "Xatolik", "Amal qilish muddati noto'g'ri, qaytadan kiriting")
            self.add_date.setFocus()
            return

        QMessageBox.information(self, "Muvaffaqiyatli", "To'lov amalga oshirildi, Salomat bo'ling")


class AdminPage(QWidget):
    def __init__(self, items: list) -> None:
        super().__init__()
        self.medicine_items = items
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
                background-color: #11182d;
                gridline-color: #4B0082;
                color: #fff;
                font-size: 25px;
            }
            QHeaderView::section {
                background-color: #221142;
                color: white;
                font-size: 25px;
                padding: 5px;
                border: 1px solid #4B0082;
            }
            QTableView::item {
                padding: 5px;
                color: #000000;
                font-size: 25px;
                font-family: sans-serif;
            }""")

        self.initUI()

    def initUI(self):
        self.core = Database()
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.hbox2 = QVBoxLayout()
        self.left_box = QHBoxLayout()

        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Search")
        self.line_edit.setFixedSize(400, 50)
        self.hbox.addStretch(10)
        self.hbox.addWidget(self.line_edit)
        self.hbox.addStretch(10)

        self.exit = Button("Exit")
        self.exit.clicked.connect(self.exit_sys)
        self.exit.setFixedSize(150, 50)

        self.madicine_table = QTableView(self)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Id", "Product", "Produced time", "End time", "Term", "Price", "Count"])

        self.add_data_to_model(self.medicine_items)

        self.madicine_table.setModel(self.model)

        self.madicine_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        colorful_delegate = ColorfulDelegate(self)

        self.madicine_table.setItemDelegate(colorful_delegate)


        delegate = ColorfulDelegate(font_size=20, cell_height=60)
        delegate.apply_delegate(self.madicine_table)


        self.update_product = Button("Update")
        self.update_product.clicked.connect(self.update_poduct_database)
        self.delete_product = Button("Delete")
        self.delete_product.clicked.connect(self.delete_product_func)

        self.expired_product = Button("Expired")
        self.expired_product.clicked.connect(self.show_expired_items)
        self.delete_expired = Button("Delete Exp")
        # self.delete_expired.setEnabled(False)
        self.delete_expired.clicked.connect(self.delete_expired_items)



        self.add_product = Button("Add")
        self.add_product.clicked.connect(self.add_product_database)
        
        self.left_box.addWidget(self.add_product)
        self.left_box.addWidget(self.update_product)
        self.left_box.addWidget(self.delete_product)
        self.left_box.addWidget(self.expired_product)
        self.left_box.addWidget(self.delete_expired)

        self.hbox2.addWidget(self.madicine_table)
        self.hbox2.addLayout(self.left_box)
        self.hbox.addStretch()
        self.hbox.addWidget(self.exit)

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox2)
        self.setLayout(self.vbox)

        self.line_edit.textChanged.connect(self.search_items)
        self.madicine_table.clicked.connect(self.on_cell_clicked)
        self.show()


    def show_expired_items(self):
        expired_items = []
        
        for row in range(self.model.rowCount()):
            end_date_str = self.model.item(row, 3).text()
            try:
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
                if end_date < datetime.now():
                    expired_items.append(row)
            except ValueError:

                QMessageBox.warning(self, "Error", f"Invalid date format in row {row + 1}. Expected yyyy-mm-dd.")
                return
        
        if expired_items:
        
            for row in range(self.model.rowCount()):
                if row in expired_items:
                    self.madicine_table.setRowHidden(row, False)
                else:
                    self.madicine_table.setRowHidden(row, True)
                    
            self.delete_product.setEnabled(True) 
        else:
            QMessageBox.information(self, "No Expired Items", "Muddati o'tgan mahsulotlar mavjud emas.")
            self.delete_product.setEnabled(False) 


    def show_all_items(self):
        all_items = self.core.Get_all_medicine_items()
        self.add_data_to_model(all_items) 
        self.madicine_table.setRowHidden(0, False) 

    def delete_expired_items(self):
        for row in range(self.model.rowCount() - 1, -1, -1):
            if not self.madicine_table.isRowHidden(row): 
                _id = self.model.item(row, 0).text()
                try:
                    success = self.core.delete_medicine(int(_id)) 
                    if not success:
                        QMessageBox.warning(self, "Error", f"Mahsulot ID {_id} o'chirilishda xato yuz berdi.")
                        continue
                    self.model.removeRow(row) 
                except Exception as e:
                    QMessageBox.warning(self, "Error", f"Mahsulot ID {_id} o'chirishda xato: {str(e)}")
                    continue 

        QMessageBox.information(self, "Success", "Muddati o'tgan mahsulotlar o'chirildi va arxivga saqlandi.")
        self.delete_product.setEnabled(False) 
        self.show_all_items()





        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(10, 15, 31))


    def search_items(self):
        search_term = self.line_edit.text().lower()
        for row in range(self.model.rowCount()):
            item = self.model.item(row, 1)
            if search_term in item.text().lower():
                self.madicine_table.setRowHidden(row, False)
            else:
                self.madicine_table.setRowHidden(row, True)

    def on_cell_clicked(self, index):
        if index.column() == 1:
            data = self.model.itemFromIndex(index).text()
            self.line_edit.setText(data)

    def add_data_to_model(self, data):
        if self.model.rowCount() == 0:
            for row in data:
                items = [QStandardItem(str(field)) for field in row]
                self.model.appendRow(items)
        else:
            self.model.removeRows(0, self.model.rowCount())
            self.line_edit.clear()
            for row in data:
                items = [QStandardItem(str(field)) for field in row]
                self.model.appendRow(items)
    
    
    def add_product_database(self):
        self.add_product_page = AddProductPage()


    def update_poduct_database(self):
        success = True
        for row in range(self.model.rowCount()):
            product_dic = {}
            _id = self.model.item(row, 0).text()
            product = self.model.item(row, 1).text()
            produced_time = self.model.item(row, 2).text()
            end_time = self.model.item(row, 3).text()
            muddati = self.model.item(row, 4).text()
            narxi = self.model.item(row, 5).text()
            soni = self.model.item(row, 6).text()

            product_dic = {
                "id": int(_id),
                "name": product,
                "produced_time": produced_time,
                "end_time": end_time,
                "expiration_date": int(muddati),
                "price": int(narxi),
                "count": int(soni)
            }

    
            update_result = self.core.update_medicine(product_dic)
            if isinstance(update_result, str):
                QMessageBox.warning(self, "Error", f"Bu mahsulotdan bor ID {_id}: {update_result}")
                success = False
            elif update_result == 0:
                QMessageBox.warning(self, "Error", f"Product with ID {_id} does not exist.")
                success = False

        if success:
            QMessageBox.information(self, "Success", "Ma'lumot xotiraga muvaffaqqiyatli saqlandi.")


    def exit_sys(self):
        self.close()

    def delete_product_func(self):
        # self.core = Database()
        
        name = self.line_edit.text()
        product = {
            'name' : name
        }
        err = self.core.delete_user_data(product)
        if err:
            QMessageBox.information(self, err)
        
        product_data = self.core.Get_all_users_data()
        product_list = [list(product) for product in product_data]
        self.add_data_to_model(product_list)


class AddProductPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(900, 950)
        self.setWindowIcon(QIcon("logo.png"))
        self.setWindowTitle("Add Product")
        self.show()
        self.UI_init()
        self.setStyleSheet("""
            QLabel{
                font-size: 30px;
                color: #000;
                font-family: sans-serif;
            }
        """)
        self.db = Database()

    def UI_init(self):
        self.core = Database()
        self.v_box = QVBoxLayout()

        self.name_lable = QLabel("Add a new product name:")
        self.add_product_name = Edit("...")

        self.time_lable = QLabel("Add produced time (yyyy-mm-dd):")   
        self.add_product_time = Edit("...")

        self.end_lable = QLabel("Add end time (yyyy-mm-dd):")
        self.add_product_end = Edit("...")
    
        self.price_lable = QLabel("Add product price:")        
        self.add_product_price = Edit("...")

        self.count_lable = QLabel("Add product count:")
        self.add_product_count = Edit("...")


        self.info_label = QLabel()
        self.save_btn = Button("Save")
        self.save_btn.clicked.connect(self.save_product)

        self.v_box.addWidget(self.name_lable, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.add_product_name, 0, Qt.AlignCenter)
        self.v_box.addStretch(3)


        self.v_box.addWidget(self.time_lable, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.add_product_time, 0, Qt.AlignCenter)
        self.v_box.addStretch(3)

        self.v_box.addWidget(self.end_lable, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.add_product_end, 0, Qt.AlignCenter)
        self.v_box.addStretch(3)

        self.v_box.addWidget(self.price_lable, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.add_product_price, 0, Qt.AlignCenter)
        self.v_box.addStretch(3)

        self.v_box.addWidget(self.count_lable, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.add_product_count, 0, Qt.AlignCenter)
        self.v_box.addStretch(3)

        self.v_box.addWidget(self.info_label, 0, Qt.AlignCenter)
        self.v_box.addWidget(self.save_btn, 0, Qt.AlignCenter)

        self.setLayout(self.v_box)

        self.info_label.setStyleSheet("""
            color: red;
        """)
    

    def save_product(self):
        name = self.add_product_name.text()
        produced_time = self.add_product_time.text()
        end_time = self.add_product_end.text()
        price = self.add_product_price.text()
        count = self.add_product_count.text()

        try:

            produced_date = datetime.strptime(produced_time, '%Y-%m-%d')
            end_date = datetime.strptime(end_time, '%Y-%m-%d')
            current_date = datetime.now()

            if end_date < current_date:
                self.info_label.setText("Error: Yaroqliligi tugash vaqti hozirgi vaqtdan kichik bolmasligi kerak.")
                return
            if produced_date > current_date:
                self.info_label.setText("Error: Ishlab chiqarilgan vaqti hozirgi vaqtdan katta bo'lmasligi kerak.")
                return
            if end_date <= produced_date:
                self.info_label.setText("Error: Yaroqliligi tugash vaqti ishlab chiqarilgan vaqtidan katta bo'lishi kerak.")
                return

            expiration_date = end_date.year - produced_date.year
            if (end_date.month, end_date.day) < (produced_date.month, produced_date.day):
                expiration_date -= 1

        except ValueError:
            self.info_label.setText("Error: Noto'g'ri format! Use yyyy-mm-dd.")
            return


        data = {
            'name': name,
            'produced_time': produced_time,
            'end_time': end_time,
            'expiration_date': expiration_date,
            'price': price,
            'count': count
        }

        result = self.db.insert_product(data)
        self.info_label.setText(result)


app = QApplication([])
login_page = mainPage()
app.exec_()