from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton
from core_test import insert_user
# PyQt5'dagi oddiy ilova uchun kod
class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.info_label = QLabel(self)
        self.info2_label = QLabel(self)

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        self.info_label.setText("")
        self.info2_label.setText("")

        # Bu tugma bosilganda insert_user funksiyasi chaqiriladi
        button = QPushButton('Insert User', self)
        button.clicked.connect(self.on_insert_user)

        vbox.addWidget(self.info_label)
        vbox.addWidget(self.info2_label)
        vbox.addWidget(button)

        self.setLayout(vbox)

    def on_insert_user(self):
        # Misol uchun, ma'lumotlar
        data = {
            'username': 'new_user',
            'password': 'password123',
            'phone_number': '+998901234567'
        }

        # Ma'lumotlarni kiriting va xatoliklarni QLabel'larda chiqaring
        insert_user(data, self.info_label, self.info2_label)

# Ilovani ishga tushirish
if __name__ == '__main__':
    app = QApplication([])
    ex = MyApp()
    ex.show()
    app.exec_()
