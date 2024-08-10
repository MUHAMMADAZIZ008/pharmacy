from PyQt5.QtWidgets import QLineEdit, QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import Qt

class PhoneLineEdit(QLineEdit):
    def __init__(self, prefix="", parent=None):
        super().__init__(parent)
        self.prefix = prefix
        self.setText(self.prefix)  # Prefiksni boshlang'ich matn sifatida o'rnatish
        self.setCursorPosition(len(self.prefix))
        self.textChanged.connect(self.on_text_changed)

    def on_text_changed(self, text):
        # Foydalanuvchi prefiksni o'zgartirsa, matnni qayta o'rnatamiz
        if not text.startswith(self.prefix):
            self.setText(self.prefix)
            self.setCursorPosition(len(self.prefix))

    def keyPressEvent(self, event):
        # Prefiksning ortida bo'lsa, Backspace tugmasini to'g'ri ishlashini ta'minlash
        if self.cursorPosition() <= len(self.prefix) and event.key() == Qt.Key_Backspace:
            return
        super().keyPressEvent(event)

    def focusInEvent(self, event):
        if self.text() == self.prefix:
            self.setText("")  # Fokusni olganda prefiksni o'chirib tashlaymiz
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        if len(self.text()) == 0:
            self.setText(self.prefix)  # Fokusdan chiqqanda prefiksni qaytaramiz
        super().focusOutEvent(event)

    def text(self):
        # Foydalanuvchi kiritgan matnni olish, prefiks bilan birga
        return super().text()  # `super().text()` prefiks bilan birga qaytaradi
