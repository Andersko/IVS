'''!
Module for MainWindow logic

@file mainwindow.py
@author Adam Kostolányi
@author Filip Solich
@date 27.3.2022
'''
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.first_input = True

        self.ui.Button_Zero.clicked.connect(self.add_0)
        self.ui.Button_One.clicked.connect(self.add_1)
        self.ui.Button_Two.clicked.connect(self.add_2)
        self.ui.Button_Three.clicked.connect(self.add_3)
        self.ui.Button_Four.clicked.connect(self.add_4)
        self.ui.Button_Five.clicked.connect(self.add_5)
        self.ui.Button_Six.clicked.connect(self.add_6)
        self.ui.Button_Seven.clicked.connect(self.add_7)
        self.ui.Button_Eight.clicked.connect(self.add_8)
        self.ui.Button_Nine.clicked.connect(self.add_9)
        self.ui.Button_Dot.clicked.connect(self.add_dot)
        self.ui.Button_Equals.clicked.connect(self.calculate)
        self.ui.Button_Plus.clicked.connect(self.add_plus)
        self.ui.Button_Minus.clicked.connect(self.add_minus)
        self.ui.Button_Times.clicked.connect(self.add_times)
        self.ui.Button_Divide.clicked.connect(self.add_divide)
        self.ui.Button_Power.clicked.connect(self.add_power)
        self.ui.Button_Sqrt.clicked.connect(self.add_root)
        self.ui.Button_Factorial.clicked.connect(self.add_factorial)
        self.ui.Button_Percent.clicked.connect(self.add_mod)
        self.ui.Button_C.clicked.connect(self.clear_input)
        self.ui.Button_Hint.clicked.connect(self.hint)

    def add_input_char(self, ch):
        if self.first_input:
            self.ui.OutputLabel.clear()
            self.first_input = False

        self.ui.OutputLabel.setText(self.ui.OutputLabel.text() + ch)

    def clear_input(self):
        self.ui.OutputLabel.clear()
        self.add_input_char('0')
        self.first_input = True

    def add_0(self):
        self.add_input_char('0')

    def add_1(self):
        self.add_input_char('1')

    def add_2(self):
        self.add_input_char('2')

    def add_3(self):
        self.add_input_char('3')

    def add_4(self):
        self.add_input_char('4')

    def add_5(self):
        self.add_input_char('5')

    def add_6(self):
        self.add_input_char('6')

    def add_7(self):
        self.add_input_char('7')

    def add_8(self):
        self.add_input_char('8')

    def add_9(self):
        self.add_input_char('9')

    def add_dot(self):
        self.add_input_char('.')

    def calculate(self):
        pass

    def add_plus(self):
        self.add_input_char('+')

    def add_minus(self):
        self.add_input_char('-')

    def add_times(self):
        self.add_input_char('*')

    def add_divide(self):
        self.add_input_char('/')

    def add_power(self):
        self.add_input_char('^')

    def add_root(self):
        self.add_input_char('√')

    def add_factorial(self):
        self.add_input_char('!')

    def add_mod(self):
        self.add_input_char('%')

    def hint(self):
        pass

    def keyPressEvent(self, event):
        numbers = (
            Qt.Key_0, Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4,
            Qt.Key_5, Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9,
        )

        if event.key() in numbers:
            getattr(self, f'add_{event.text()}')()
        elif event.key() in (Qt.Key_Comma, Qt.Key_Period):
            self.add_dot()
        elif event.key() in (Qt.Key_Equal, Qt.Key_Enter, Qt.Key_Return):
            self.calculate()
        elif event.key() == Qt.Key_Plus:
            self.add_plus()
        elif event.key() == Qt.Key_Minus:
            self.add_minus()
        elif event.key() == Qt.Key_Asterisk:
            self.add_times()
        elif event.key() == Qt.Key_Slash:
            self.add_divide()
        elif event.key() == Qt.Key_AsciiCircum:
            self.add_power()
        elif event.key() == Qt.Key_Percent:
            self.add_mod()
        elif event.key() == Qt.Key_Exclam:
            self.add_factorial()
        elif event.key() == Qt.Key_Question:
            self.hint()
        elif event.key() == Qt.Key_Delete:
            self.clear_input()
        elif event.key() == Qt.Key_Backspace:
            old = self.ui.OutputLabel.text()
            self.ui.OutputLabel.setText(old[:len(old)-1])
