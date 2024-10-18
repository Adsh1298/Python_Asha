from qtpy.QtWidgets import (QApplication, QWidget, QVBoxLayout, QTableWidget,
                            QTableWidgetItem,QPushButton, QMessageBox)
class DbForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MySQL DB Program")
        self.resize(400, 400)
        self.layout()