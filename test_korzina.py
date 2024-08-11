from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTableView, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QHeaderView, QLabel
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon, QPainter, QColor
from PyQt5.QtCore import Qt

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
        self.navbar_box = QHBoxLayout()
        self.hbox2 = QHBoxLayout()

        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("Mahsulot nomini kiriting")
        self.search_edit.setFixedSize(400, 50)
        self.navbar_box.addStretch(20)
        self.navbar_box.addWidget(self.search_edit)
        self.navbar_box.addStretch(1)

        self.amount = QLineEdit()
        self.amount.setPlaceholderText("Miqdori")
        self.amount.setFixedSize(100, 50)
        self.navbar_box.addWidget(self.amount)

        self.add_btn = QPushButton("Add")
        self.add_btn.setFixedSize(100, 50)
        self.navbar_box.addWidget(self.add_btn)
        self.navbar_box.addStretch(10)

        self.card_btn = QPushButton("Korzina 🧺")
        self.card_btn.setFixedSize(150, 50)
        self.navbar_box.addWidget(self.card_btn)

        self.Korzina_items = QListWidget()
        self.Korzina_items.maximumHeight()

        self.exit = QPushButton("Chiqish")
        self.exit.setFixedSize(150, 50)
        self.navbar_box.addWidget(self.exit)

        self.users_infos = QTableView(self)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Product", "Produced time", "End time", "Muddati", "Narxi"])

        self.add_data_to_model(self.medicine_items)

        self.users_infos.setModel(self.model)

        self.users_infos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.hbox2.addWidget(self.users_infos, 3)
        self.hbox2.addWidget(self.Korzina_items, 1)

        self.users_infos.setEditTriggers(QTableView.NoEditTriggers)

        self.navbar_box.addStretch()

        self.vbox.addLayout(self.navbar_box)
        self.vbox.addLayout(self.hbox2)
        self.setLayout(self.vbox)

        self.add_btn.clicked.connect(self.add_to_cart)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(255, 255, 200))

    def add_to_cart(self):
        # Mahsulot nomi va miqdorini olish
        product_name = self.search_edit.text()
        amount_text = self.amount.text()

        if product_name and amount_text.isdigit():
            quantity = int(amount_text)

            # Mahsulotni Korzinka'ga qo'shish
            item_widget = QWidget()
            item_layout = QHBoxLayout()
            label = QLabel(f"{product_name} - {quantity} ta")
            remove_button = QPushButton("Remove")
            item_layout.addWidget(label)
            item_layout.addWidget(remove_button)
            item_widget.setLayout(item_layout)

            list_item = QListWidgetItem()
            list_item.setSizeHint(item_widget.sizeHint())
            self.Korzina_items.addItem(list_item)
            self.Korzina_items.setItemWidget(list_item, item_widget)

            remove_button.clicked.connect(lambda checked, item=list_item: self.remove_item(item))

            # Maydonlarni tozalash
            self.search_edit.clear()
            self.amount.clear()

    def remove_item(self, item):
        row = self.Korzina_items.row(item)
        self.Korzina_items.takeItem(row)

    def add_data_to_model(self, data):
        if self.model.rowCount() > 0:
            self.model.removeRows(0, self.model.rowCount())
            self.search_edit.clear()

        for row in data:
            items = [QStandardItem(str(field)) for field in row]

            if items:
                last_item = items[-2]
                last_item.setText(f"{last_item.text()} so'm")

            self.model.appendRow(items[1:-1])

if __name__ == "__main__":
    app = QApplication([])
    items = [
        (1, "Product A", "2024-01-01", "2025-01-01", 1, 10000, 120),
        (2, "Product B", "2024-02-01", "2025-02-01", 1, 15000, 230),
        (3, "Product C", "2024-03-01", "2025-03-01", 1, 20000, 234)
    ]
    window = Medicine_buy(items)
    app.exec_()
