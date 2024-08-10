from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTableView, QHeaderView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class Medicine_buy(QWidget):
    def __init__(self, items: list) -> None:
        super().__init__()
        self.medicine_items = items
        print(self.medicine_items)
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
            }""")

        self.initUI()

    def initUI(self):
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.hbox2 = QHBoxLayout()

        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Search")
        self.line_edit.setFixedSize(400, 50)
        self.hbox.addStretch(10)
        self.hbox.addWidget(self.line_edit)
        self.hbox.addStretch(10)

        self.card_btn = QPushButton("Card 🧺", self)
        self.card_btn.setFixedSize(150, 50)
        self.exit = QPushButton("Exit", self)
        self.exit.setFixedSize(150, 50)

        self.users_infos = QTableView(self)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Product", "Produced time", "End time", "Muddati", "Narxi"])

        self.add_data_to_model(self.medicine_items)

        self.users_infos.setModel(self.model)

        self.users_infos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.hbox2.addWidget(self.users_infos)

        self.hbox.addStretch()
        self.hbox.addWidget(self.card_btn)
        self.hbox.addWidget(self.exit)

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox2)
        self.setLayout(self.vbox)

        # Connect the textChanged signal to the search method
        self.line_edit.textChanged.connect(self.search_items)

        self.show()

    def search_items(self):
        search_term = self.line_edit.text().lower()
        for row in range(self.model.rowCount()):
            item = self.model.item(row, 0)  # Assuming column 0 has the product name
            if search_term in item.text().lower():
                self.users_infos.setRowHidden(row, False)
            else:
                self.users_infos.setRowHidden(row, True)

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

# class Medicine_buy(QWidget):
#     def __init__(self, items: list) -> None:
#         self.medicine_items = items
#         print(self.medicine_items)
#         super().__init__()
#         self.showMaximized()
#         self.setWindowTitle("Najot Pharmacy")
#         self.setWindowIcon(QIcon("login_icon.png"))

#         self.setStyleSheet("""
#             QHBoxLayout{
#                 background: yellow;
#                     }
#             QLineEdit{
#                 background: #F5F5F5;
#                 font-size: 25px;
#                 border-radius: 10px;
#                 padding: 5px;
#                 padding-left: 10px
        
#                     }
                    
#             QPushButton{
#                 background-color: #4B0082;
#                 color: white;
#                 font-size: 25px;
#                 border-radius: 10px;
#                 padding: 5px;
#                 padding-left: 10px
#                            }""")

#         self.initUI()

#     def initUI(self):

#         self.vbox = QVBoxLayout()

#         self.hbox = QHBoxLayout()
#         self.hbox2 = QHBoxLayout()

#         self.line_edit = QLineEdit(self)
#         self.line_edit.setPlaceholderText("Search")
#         self.line_edit.setFixedSize(400, 50)
#         self.hbox.addStretch(10)
#         self.hbox.addWidget(self.line_edit)
#         self.hbox.addStretch(10)

#         self.card_btn = QPushButton("Card 🧺", self)
#         self.card_btn.setFixedSize(150, 50)
#         self.exit = QPushButton("Exit", self)
#         self.exit.setFixedSize(150, 50)


#         self.users_infos = QTableView(self)
        
#         self.model = QStandardItemModel()
#         self.model.setHorizontalHeaderLabels(["Product", "Produced time", "End time", "Muddati", "Narxi"])

#         self.add_data_to_model(self.medicine_items)

#         self.users_infos.setModel(self.model)

#         self.users_infos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
#         self.hbox2.addWidget(self.users_infos)

#         self.hbox.addStretch()
#         self.hbox.addWidget(self.card_btn)
#         self.hbox.addWidget(self.exit)

#         self.vbox.addLayout(self.hbox)
#         self.vbox.addLayout(self.hbox2)
#         self.setLayout(self.vbox)

#         self.users_infos.clicked.connect(self.on_cell_clicked)
        
#         self.show()

#     def on_cell_clicked(self, index):
#         if index.column() == 0: 
#             data = self.model.itemFromIndex(index).text()
#             self.line_edit.setText(data)

#     def add_data_to_model(self, data):
#         if self.model.rowCount() == 0:
#             for row in data:
#                 items = [QStandardItem(str(field)) for field in row]
#                 self.model.appendRow(items[1:-1])
#         else:
#             self.model.removeRows(0, self.model.rowCount())
#             self.line_edit.clear()
#             for row in data:
#                 items = [QStandardItem(str(field)) for field in row]
#                 self.model.appendRow(items[1:-1])