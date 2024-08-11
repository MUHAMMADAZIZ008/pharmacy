from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QPushButton, QLabel, QHBoxLayout

class MainPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Page")

        self.layout = QVBoxLayout()

        # QListWidget yaratish
        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)

        # 10 ta elementni qo'shish
        self.items = []
        for i in range(10):
            item_widget = QWidget()
            item_layout = QHBoxLayout()
            button = QPushButton(f"Button {i+1}")
            label = QLabel(f"Item {i+1}")
            item_layout.addWidget(button)
            item_layout.addWidget(label)
            item_widget.setLayout(item_layout)

            list_item = QListWidgetItem()
            list_item.setSizeHint(item_widget.sizeHint())
            self.list_widget.addItem(list_item)
            self.list_widget.setItemWidget(list_item, item_widget)

            # Yozuvlarni saqlash
            self.items.append((label.text(),))

        # O'tish tugmasi
        self.next_button = QPushButton("Next Page")
        self.layout.addWidget(self.next_button)

        self.next_button.clicked.connect(self.open_next_page)

        self.setLayout(self.layout)

    def open_next_page(self):
        # Yangi oyna yaratish
        self.next_page_window = QWidget()
        self.next_page_window.setWindowTitle("Next Page")
        next_layout = QVBoxLayout()

        # Yangi QListWidget yaratish va yozuvlarni qo'shish
        new_list_widget = QListWidget()

        for text in self.items:
            item_widget = QWidget()
            item_layout = QHBoxLayout()
            label = QLabel(text[0])  # Faqat yozuvni qo'shish
            item_layout.addWidget(label)
            item_widget.setLayout(item_layout)

            new_item = QListWidgetItem()
            new_item.setSizeHint(item_widget.sizeHint())
            new_list_widget.addItem(new_item)
            new_list_widget.setItemWidget(new_item, item_widget)

        next_layout.addWidget(new_list_widget)

        # Sahifa uchun Layout qo'shish
        self.next_page_window.setLayout(next_layout)
        self.next_page_window.show()  # Yangi oynani ko'rsatish

app = QApplication([])
window = MainPage()
window.show()
app.exec_()
