from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QTableView,
    QHeaderView,
    QPushButton,
    QMessageBox,
    QHBoxLayout,
    QLineEdit,
    QHeaderView
)

from PyQt5.QtGui import   QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QBrush, QColor, QIcon
from core import *

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
        self.core = Database()
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

        self.exit = QPushButton("Exit")
        self.exit.clicked.connect(self.exit_sys)
        self.exit.setFixedSize(150, 50)

        self.madicine_table = QTableView(self)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Product", "Produced time", "End time", "Muddati", "Narxi"])

        self.add_data_to_model(self.medicine_items)

        self.madicine_table.setModel(self.model)

        self.madicine_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Delegate removed for simplification
        # delegate = ColorfulDelegate(self)
        # self.madicine_table.setItemDelegate(delegate)

        # Left panel buttons
        self.update_product = QPushButton("Update")
        self.update_product.clicked.connect(self.update_database)
        self.delete_product = QPushButton("Delete")
        self.expired_product = QPushButton("Expired")
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
        painter.fillRect(self.rect(), QColor(255, 255, 200))  # Faqat oq fonda chizish

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
                self.model.appendRow(items)
        else:
            self.model.removeRows(0, self.model.rowCount())
            self.line_edit.clear()
            for row in data:
                items = [QStandardItem(str(field)) for field in row]
                self.model.appendRow(items)

    def update_database(self):


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

if __name__ == '__main__':
    app = QApplication([])
    window = AdminPage()
    window.show()
    app.exec_()
