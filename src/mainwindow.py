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
import re
import my_math

class MainWindow(QMainWindow):


    precTable = [
#stack +-     *,/     (      )     !       ^      √      %       $      # next
    ['R',   'R',   'S',   'R',   'R',   'R',   'ERR', 'ERR', 'ERR'],    # +-
    ['S',   'R',   'S',   'R',   'R',   'R',   'ERR', 'ERR', 'ERR'],    # */
    ['S',   'S',   'S',   'ERR', 'R',   'S',   'S',   'ERR', 'ERR'],    # (
    ['R',   'R',   'ERR', 'R',   'R',   'R',   'R',   'ERR', 'ERR'],    # )
    ['S',   'S',   'S',   'R',   'R',   'R',   'ERR', 'ERR', 'ERR'],    # !
    ['S',   'S',   'S',   'R',   'R',   'S',   'ERR', 'ERR', 'ERR'],    # ^ todo
    ['S',   'S',   'S',   'ERR', 'ERR', 'S',   'ERR', 'ERR', 'ERR'],    # √ todo
    ['ERR', 'ERR', 'ERR', 'ERR', 'ERR', 'ERR', 'ERR', 'ERR', 'ERR'],    # % todo
    ['R',   'R',   'ERR', 'ERR', 'R',   'R',   'ERR', 'R',   'A']]      #$            

    def getIndex(self, operator):
        if operator == '+' or operator == '-':
            return 0
        elif operator == '*' or  operator == '/':
            return 1
        elif operator == '(':
            return 2
        elif operator == ')':
            return 3
        elif operator == '!':
            return 4
        elif operator == '^':
            return 5
        elif operator == '√':
            return 6
        elif operator == '%':
            return 7
        elif operator == '$':
            return 8

    def shift(self):
        pass

    def reduce(self,numbers,operations):
        pass

    def parse_expression(self, operation, numberList):
        result = 0.0
        if operation == '+':
            result = my_math.add(numberList.pop(),numberList.pop())
        elif operation == '-':
            result = my_math.subtract(numberList.pop(),numberList.pop())
        elif operation == '*':
            result = my_math.multiply(numberList.pop(),numberList.pop())
        elif operation == '/':
            result = my_math.divide(numberList.pop(),numberList.pop())
        elif operation == '!':
            result = my_math.factorial(numberList.pop())
        elif operation == '^':
            last = numberList.pop()
            preLast = numberList.pop()
            result = my_math.power(preLast,last)
        elif operation == '√':
            my_math.root(numberList.pop())
        elif operation == '%':
            last = numberList.pop()
            preLast = numberList.pop()
            result = my_math.modulo(preLast,last)
        
        numberList.append(result)

        

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


    def button_pressed(self):
        self.add_input_char(self.sender().text()[-1])

    def add_input_char(self, ch):
        if self.first_input:
            self.ui.OutputLabel.clear()
            self.first_input = False

        self.ui.OutputLabel.setText(self.ui.OutputLabel.text() + ch)

    def clear_input(self):
        self.ui.OutputLabel.clear()
        self.add_input_char('0')
        self.first_input = True

    def calculate(self):
        expression = str(self.ui.OutputLabel.text())
        
        numbers = self.parseNumbers(expression)
        operations = self.parseOperations(expression)
        numbers.reverse()
        numbers.insert(0,'$')
        operations.reverse()
        operations.insert(0,'$')
        operations.insert(0,'$')
        print(numbers)
        print(operations)
        print('--------------WHILE--------------')
        operationsStack = []
        numbersStack = []
        while True:
            print('-----------Begin----------')
            currentOperator = operations.pop()
            nextOperator = operations[-1]
            print(currentOperator + '\t'+ nextOperator)
            print(operations)
            print(operationsStack)
            print(numbers)
            print(numbersStack)
            # if (currentOperator == '(' and nextOperator == ')'):
            #     operations.pop()
            #     operations.append(operationsStack.pop())
            #     numbers.append(numbersStack.pop())
            #     print('-------Parenthesis pop--------')
            #     continue

            if self.precTable[self.getIndex(nextOperator)][self.getIndex(currentOperator)] == 'S':
                operationsStack.append(currentOperator)
                if (nextOperator != '('):
                    numbersStack.append(numbers.pop())
                print("SHIFT")
            elif self.precTable[self.getIndex(nextOperator)][self.getIndex(currentOperator)] == 'R':
                print("REDUCE")
                self.parse_expression(currentOperator,numbers)
                if (len(operationsStack) != 0 ):
                    if( operationsStack[-1]== '(' and nextOperator== ')'):
                        operations.pop()
                        operationsStack.pop()
                        print('-------Parenthesis pop--------')
                    operations.append(operationsStack.pop())
                    numbers.append(numbersStack.pop())
                    
                #if (len(operationsStack) != 0 and nextOperator== ')' and operationsStack[-1]== '('):
                #if (nextOperator == ')' and operationsStack[-1]== '(')
                #if (len(numbersStack) != 0 and operationsStack[0] != '('):
                #   print(operationsStack[0])
                    
            elif self.precTable[self.getIndex(nextOperator)][self.getIndex(currentOperator)] == 'ERR':
                print("ERROR")
                return
            elif self.precTable[self.getIndex(nextOperator)][self.getIndex(currentOperator)] == 'A':
                print("END")
                print(numbers)
                self.ui.OutputLabel.setText(str(numbers[-1]))
                self
                return
            print('---------AFTER----------')
            print(operations)
            print(operationsStack)
            print(numbers)
            print(numbersStack)
            print('-----------END-----------')
        pass

    def hint(self):
        pass

    def parseNumbers(self,text):
        parsedNumbers = re.split(r"\+|-|\/|\*|√|^|\!|\(|\)",text)
        parsedNumbers = list(filter(None, parsedNumbers))
        parsedNumbers = [float(x) for x in parsedNumbers]
        return parsedNumbers

    def parseOperations(self,text):
        parseOperations = re.split(r"[0-9]*\.?[0-9]*",text)
        return list(filter(None, parseOperations))

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
        elif event.key() == Qt.Key_Question:
            self.hint()
        elif event.key() == Qt.Key_Delete:
            self.clear_input()
        elif event.key() == Qt.Key_Backspace:
            self.ui.OutputLabel.setText(self.ui.OutputLabel.text()[:-1])
