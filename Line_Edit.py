from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt

class PhoneLineEdit(QLineEdit):
    def __init__(self, prefix="", parent=None):
        super().__init__(parent)
        self.prefix = prefix
        self.setPlaceholderText(self.prefix)
        self.textChanged.connect(self.enforce_prefix)

    def enforce_prefix(self, text):
        if not text.startswith(self.prefix):
            self.setText(self.prefix)
            self.setCursorPosition(len(self.prefix))

    def keyPressEvent(self, event):
        if self.cursorPosition() <= len(self.prefix) and event.key() == Qt.Key_Backspace:
            return
        super().keyPressEvent(event)

    def focusInEvent(self, event):
        if self.text() == self.prefix:
            self.setText("")
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        if len(self.text()) == 0:
            self.setText(self.prefix)
        super().focusOutEvent(event)
