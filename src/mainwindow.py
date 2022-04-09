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
#prev +-     *,/     (      )     !       ^      √      %       $      # current
    ['R',   'R',   'S',   'R',   'R',   'R',   'ERR', 'ERR', 'S'],    # +-
    ['S',   'R',   'S',   'R',   'R',   'R',   'ERR', 'ERR', 'S'],    # */
    ['S',   'S',   'S',   'ERR', 'R',   'S',   'S',   'ERR', 'S'],    # (
    ['R',   'R',   'ERR', 'R',   'R',   'R',   'R',   'ERR', 'S'],    # )
    ['S',   'S',   'S',   'R',   'R',   'R',   'ERR', 'ERR', 'S'],    # !
    ['S',   'S',   'S',   'R',   'R',   'S',   'ERR', 'ERR', 'S'],    # ^ todo
    ['S',   'S',   'S',   'ERR', 'ERR', 'S',   'ERR', 'ERR', 'S'],    # √ todo
    ['ERR', 'ERR', 'ERR', 'ERR', 'ERR', 'ERR', 'ERR', 'ERR', 'S'],    # % todo
    ['R',   'R',   'ERR', 'R', 'R',   'R',   'ERR', 'R',   'A']]      #$            

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
            print("operation +")
            result = my_math.add(numberList.pop(),numberList.pop())
        elif operation == '-':
            print("operation -")
            last = numberList.pop()
            preLast = numberList.pop()
            result = my_math.subtract(preLast,last)
        elif operation == '*':
            print("operation *")
            result = my_math.multiply(numberList.pop(),numberList.pop())
        elif operation == '/':
            print("operation /")
            last = numberList.pop()
            preLast = numberList.pop()
            result = my_math.divide(preLast,last)
        elif operation == '!':
            print("operation !")
            result = my_math.factorial(numberList.pop())
        elif operation == '^':
            print("operation ^")
            last = numberList.pop()
            preLast = numberList.pop()
            result = my_math.power(preLast,last)
        elif operation == '√':
            print("operation sqrt")
            my_math.root(numberList.pop())
        elif operation == '%':
            print("operation %")
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
        tokens = self.parseString(expression)
        tokens.append('$')

        print('--------------PARSE START - WHILE--------------')
        operationsStack = ['$']
        numbersStack = []
        print(tokens)
        while True:
            print('-----------Begin----------')
            print(tokens)
            currentToken = tokens.pop(0)
    
            print(currentToken)
            print(tokens)
            print(numbersStack)
            print(operationsStack)  

            if isinstance(currentToken, float):
                print('push number')
                numbersStack.append(currentToken)
            elif isinstance(currentToken, str):
                
                # if first operation
                if operationsStack[-1] == '$' and len(tokens) != 0: # tokens[0] != '$':
                    print('if1')
                    operationsStack.append(currentToken)
                else:
                    print('if2')
                    prevOperator = operationsStack[-1]
                    nextAction = self.precTable[self.getIndex(currentToken)][self.getIndex(prevOperator)]
                    
                    if nextAction == 'S':
                        print('shift')
                        operationsStack.append(currentToken)
                    elif nextAction == 'R':
                        print('reduce')
                        operation = operationsStack.pop()
                        
                        pushRightParenth = False
                        if operation == ')':
                            print('this')
                            pushRightParenth = True
                            operation = operationsStack.pop()

                        self.parse_expression(operation,numbersStack)
                        
                        if currentToken != '$':
                            operationsStack.append(currentToken)
                        else:
                            tokens.insert(0,currentToken)
                            if pushRightParenth:
                                print("push )")
                                operationsStack.append(')')
                                print(operation)
                                print(tokens)
                                print(operationsStack)
                                pushRightParenth = False
                            
                            
                        if operationsStack[-1] == ')' and operationsStack[-2] == '(':
                            print('pop parenth')
                            operationsStack.pop()
                            operationsStack.pop()

                    elif nextAction == 'ERR':
                        print('error')
                    elif nextAction == "A":
                        print('a')
                        break


            print(numbersStack)
            print(operationsStack)    
            
        print(numbersStack)
        print(operationsStack)
        print('-----------END-----------')
        self.ui.OutputLabel.setText(str(numbersStack[0]))

    def hint(self):
        pass

    def parseString(self,text):
        regex = re.compile(r'((?:(?:\d+(?:\.\d+)?))|(?:[-+\/*()√^%])|(?:-?\.\d+))') #r'((?:-?(?:\d+(?:\.\d+)?))|(?:[-+\/*()])|(?:-?\.\d+))'
        parsed = re.findall(regex,text)
        parsed = [ float(x) if (re.match( r'(\d*\.\d+|\d+)' ,x) != None) else x for x in parsed]
        # print(parsed)
        # for x in parsed:
        #     print(x,type(x))
        return parsed

    def parseNumbers(self,text):
        parsedNumbers = re.split(r"\+|-|\/|\*|\√|\^|\!|\(|\)",text)
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
