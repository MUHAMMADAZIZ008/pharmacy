from PyQt5.QtWidgets import(
    QPushButton,
    QLineEdit
)

class Bottom(QPushButton):
        def __init__(self, text:str = "") -> None:
            super().__init__(text)
            self.setFixedSize(200, 50)
            self.setStyleSheet("""
            QPushButton{
                padding: 10px;
                background-color: #071952;
                color: #EBF4F6;
                font-size: 25px;
                font-family: sans-serif;
                border: 0;
                border-radius: 15px;
                font-weight: 600;
            }
            QPushButton:hover{
                background-color: #fff;
                color: #071952;
                border: 3px solid #071952;
            }
             """)


class Edit(QLineEdit):
      def __init__(self, text:str = ""):
            super().__init__()
            self.setPlaceholderText(text)
            self.setStyleSheet("""
                QLineEdit{
                    background-color: rgba(255, 255, 255, 0);
                    font-size: 25px;
                    font-family: sans-serif;
                    border: 0;
                    border-bottom: 2px solid #000;
                }
            """)


