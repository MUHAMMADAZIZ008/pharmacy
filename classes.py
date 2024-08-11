from PyQt5.QtWidgets import(
    QPushButton,
    QLineEdit
)
from PyQt5.QtCore import Qt

class Button(QPushButton):
        def __init__(self, text:str = "") -> None:
            super().__init__(text)
            self.setFixedSize(250, 50)

            self.enterEvent = self.on_enter
            self.leaveEvent = self.on_leave

            self.setStyleSheet("""
            QPushButton{
                padding: 10px;
                background-color: #FF8225;
                color: #fff;
                font-size: 25px;
                font-family: sans-serif;
                border: 0;
                border-radius: 15px;
                font-weight: 600;
            }
            QPushButton:hover{
                background-color: #03C988;
                color: #fff;
                
            }
            """)
        def on_enter(self, event):
            self.setCursor(Qt.PointingHandCursor)  
            super().enterEvent(event)

        def on_leave(self, event):
            self.setCursor(Qt.ArrowCursor)
            super().leaveEvent(event)


class Edit(QLineEdit):
      def __init__(self, text:str = ""):
            super().__init__()
            self.setPlaceholderText(text)
            self.setFixedSize(400, 50)
            self.setStyleSheet("""
                QLineEdit{
                    padding: 10px;
                    background-color: rgba(255, 255, 255, 0);
                    font-size: 25px;
                    font-family: sans-serif;
                    border: 0;
                    border-bottom: 2px solid #000;
                }
            """)


