from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QTableView,
    QStyledItemDelegate,
    QPushButton
)

from PyQt5.QtGui import   QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QBrush, QColor

class ButtonDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def paint(self, painter, option, index):
        super().paint(painter, option, index)

        if index.column() == 0:  # Assuming the button column is the first one
            button_rect = QRect(option.rect)
            button_rect.adjust(5, 5, -5, -5)
            painter.setBrush(QBrush(QColor("#4B0082")))  # Background color for the button
            painter.drawRect(button_rect)
            painter.setPen(Qt.white)
            painter.drawText(button_rect, Qt.AlignCenter, "Click Me")

    def editorEvent(self, event, model, option, index):
        if event.type() == event.MouseButtonRelease and index.column() == 0:
            print(f"Button clicked in row {index.row()}")
            return True
        return super().editorEvent(event, model, option, index)

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table with Button Column")
        self.setGeometry(300, 300, 600, 400)
        self.layout = QVBoxLayout(self)
        self.table = QTableView(self)
        self.layout.addWidget(self.table)
        self.model = QStandardItemModel(5, 2)
        self.model.setHorizontalHeaderLabels(["Action", "Data"])
        
        for row in range(5):
            button_item = QStandardItem()
            button_item.setEditable(False)
            data_item = QStandardItem(f"Item {row}, 1")
            self.model.setItem(row, 0, button_item)
            self.model.setItem(row, 1, data_item)

        self.table.setModel(self.model)
        self.delegate = ButtonDelegate(self.table)
        self.table.setItemDelegateForColumn(0, self.delegate)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWidget()
    window.show()
    app.exec_()
