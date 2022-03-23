# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

class CalculatorMainWindow(QWidget):
    def __init__(self):
        super(CalculatorMainWindow, self).__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.w =loader.load(ui_file, self)
        self.w .show()
        ui_file.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = CalculatorMainWindow()
    widget.show()
    sys.exit(app.exec())
