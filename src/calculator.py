# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from PySide6 import QtWidgets
from mainwindow import MainWindow

class calculator(QtWidgets.QMainWindow):
    def __init__(self):
        pass
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())