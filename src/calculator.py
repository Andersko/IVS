"""!
Calculator "main" file

Create application and main window

@file calculator.py
@author Filip Solich
@date 20.3.2022
"""

import sys
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.setWindowTitle('Calculator')
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
