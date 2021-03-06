"""!
Module for MainWindow logic

@file mainwindow.py
@author Adam Kostolányi
@author Filip Solich
@date 27.3.2022
"""


import re

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow

import expression_parser
from ui_hintwindow import Ui_HintWindow
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):

    """!
    Initialize the main window
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.first_input = True

        self.ui.Button_Zero.clicked.connect(self.button_pressed)
        self.ui.Button_One.clicked.connect(self.button_pressed)
        self.ui.Button_Two.clicked.connect(self.button_pressed)
        self.ui.Button_Three.clicked.connect(self.button_pressed)
        self.ui.Button_Four.clicked.connect(self.button_pressed)
        self.ui.Button_Five.clicked.connect(self.button_pressed)
        self.ui.Button_Six.clicked.connect(self.button_pressed)
        self.ui.Button_Seven.clicked.connect(self.button_pressed)
        self.ui.Button_Eight.clicked.connect(self.button_pressed)
        self.ui.Button_Nine.clicked.connect(self.button_pressed)
        self.ui.Button_Dot.clicked.connect(self.button_pressed)
        self.ui.Button_Equals.clicked.connect(self.calculate)
        self.ui.Button_Plus.clicked.connect(self.button_pressed)
        self.ui.Button_Minus.clicked.connect(self.button_pressed)
        self.ui.Button_Times.clicked.connect(self.button_pressed)
        self.ui.Button_Divide.clicked.connect(self.button_pressed)
        self.ui.Button_Power.clicked.connect(self.button_pressed)
        self.ui.Button_Sqrt.clicked.connect(self.button_pressed)
        self.ui.Button_Factorial.clicked.connect(self.button_pressed)
        self.ui.Button_Percent.clicked.connect(self.button_pressed)
        self.ui.Button_C.clicked.connect(self.clear_input)
        self.ui.Button_Hint.clicked.connect(self.hint)
        self.ui.Button_Left_Parenthesis.clicked.connect(self.button_pressed)
        self.ui.Button_Right_Parenthesis.clicked.connect(self.button_pressed)

        self.ui.OutputLabel.textChanged.connect(self.remove_leading_zero)

        self.dialog = Ui_HintWindow()
        self.dialog.setupUi(self.dialog)

    """!
    Remove the zero after text input

    @param self Reference to the current instance of the class
    """
    def remove_leading_zero(self):
        text = self.ui.OutputLabel.text()
        if len(text) > 1 and text[0] == '0':
            self.ui.OutputLabel.setText(text[1:])

    """!
    Calculate the expression

    @param self Reference to the current instance of the class
    """
    def button_pressed(self):
        self.add_input_char(self.sender().text()[-1])

    """!
    Add character to input box

    @param self Reference to the current instance of the class
    """
    def add_input_char(self, ch):
        if self.first_input:
            self.ui.OutputLabel.clear()
            self.first_input = False

        self.ui.OutputLabel.setText(self.ui.OutputLabel.text() + ch)

    """!
    Clear the input

    @param self Reference to the current instance of the class
    """
    def clear_input(self):
        self.ui.OutputLabel.clear()
        self.add_input_char('0')
        self.first_input = True

    """!
    Calculate the expression

    @param self Reference to the current instance of the class
    """
    def calculate(self):
        expression = str(self.ui.OutputLabel.text())

        result = expression_parser.parse_expression(expression)
        self.ui.OutputLabel.setText(result)
        if result == 'Bad input':
            self.first_input = True

    """!
    Show hint dialog window

    @param self Reference to the current instance of the class
    """
    def hint(self):
        self.dialog.show()

    """!
    Add character to input box based on key event

    @param self Reference to the current instance of the class
    @param event Event of the pressed key
    """
    def keyPressEvent(self, event):
        numbers = (
            Qt.Key_0, Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4,
            Qt.Key_5, Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9,
        )

        if event.key() in numbers:
            self.add_input_char(event.text())
        elif event.key() in (Qt.Key_Comma, Qt.Key_Period):
            self.add_input_char('.')
        elif event.key() in (Qt.Key_Equal, Qt.Key_Enter, Qt.Key_Return):
            self.calculate()
        elif event.key() == Qt.Key_Plus:
            self.add_input_char('+')
        elif event.key() == Qt.Key_Minus:
            self.add_input_char('-')
        elif event.key() == Qt.Key_Asterisk:
            self.add_input_char('*')
        elif event.key() == Qt.Key_Slash:
            self.add_input_char('/')
        elif event.key() == Qt.Key_AsciiCircum:
            self.add_input_char('^')
        elif event.key() == Qt.Key_Percent:
            self.add_input_char('%')
        elif event.key() == Qt.Key_Exclam:
            self.add_input_char('!')
        elif event.key() == Qt.Key_ParenLeft:
            self.add_input_char('(')
        elif event.key() == Qt.Key_ParenRight:
            self.add_input_char(')')
        elif event.key() == Qt.Key_F1:
            self.hint()
        elif event.key() == Qt.Key_Delete:
            self.clear_input()
        elif event.key() == Qt.Key_Backspace:
            self.ui.OutputLabel.setText(self.ui.OutputLabel.text()[:-1])
