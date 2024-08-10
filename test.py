from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QLineEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Dori Qidirish')
        self.setGeometry(100, 100, 600, 400)

        # Create a widget for the central area
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a QVBoxLayout for the central widget
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a QLineEdit for search input
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText('Dori nomini kiriting...')
        layout.addWidget(self.search_box)

        # Create a QTableWidget to display the drugs
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(1)  # Assume one column for drug names
        self.table_widget.setHorizontalHeaderLabels(['Dori nomi'])
        layout.addWidget(self.table_widget)

        # Example drug data
        self.drugs = [
            'Paracetamol', "Paracetamol", 'Paragina', 'Aspirin', 'Amoxicillin', 'Cough Syrup', 'Vitamin C'
        ]

        # Populate the table with the example drug data
        self.populate_table(self.drugs)

        # Connect the textChanged signal to the search method
        self.search_box.textChanged.connect(self.search_drugs)

    def populate_table(self, drugs):
        self.table_widget.setRowCount(len(drugs))
        for row, drug in enumerate(drugs):
            self.table_widget.setItem(row, 0, QTableWidgetItem(drug))

    def search_drugs(self):
        search_term = self.search_box.text().lower()
        for row in range(self.table_widget.rowCount()):
            item = self.table_widget.item(row, 0)
            if search_term in item.text().lower():
                self.table_widget.setRowHidden(row, False)
            else:
                self.table_widget.setRowHidden(row, True)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
