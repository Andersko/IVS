'''!
Module for expression parser logic

@file expression_parser.py
@author Adam Kostolányi
@date 11.4.2022
'''
import re
import my_math


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

def getIndex( operator):
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

def calculate_expression( operation, numberList):
        result = 0.0
        if operation == '+':
            print("operation +")
            print(len(numberList))
            if len(numberList) >= 2:
                last = numberList.pop()
                preLast = numberList.pop()
                result = my_math.add(preLast,last)
            else:
                return True
        elif operation == '-':
            print("operation -")
            if len(numberList) >= 2:
                last = numberList.pop()
                preLast = numberList.pop()
                result = my_math.subtract(preLast,last)
            else:
                return True
        elif operation == '*':
            print("operation *")
            if len(numberList) >= 2:
                last = numberList.pop()
                preLast = numberList.pop()
                result = my_math.multiply(preLast,last)
            else:
                return True
        elif operation == '/':
            print("operation /")
            if len(numberList) >= 2:
                last = numberList.pop()
                preLast = numberList.pop()
                result = my_math.divide(preLast,last)
            else:
                return True
        elif operation == '!':
            print("operation !")
            if len(numberList) >= 1:
                last = numberList.pop()
                result = my_math.factorial(last)
            else:
                return True
        elif operation == '^':
            print("operation ^")
            if len(numberList) >= 2:
                last = numberList.pop()
                preLast = numberList.pop()
                result = my_math.power(preLast,last)
            else:
                return True
        elif operation == '√':
            print("operation sqrt")
            if len(numberList) >= 1:
                last = numberList.pop()
                my_math.root(last)
            else:
                return True
        elif operation == '%':
            print("operation %")
            if len(numberList) >= 2:
                last = numberList.pop()
                preLast = numberList.pop()
                result = my_math.modulo(preLast,last)
            else:
                return True
        
        numberList.append(result)
        return False

def parse_string(text):
        regex = re.compile(r'((?:(?:\d+(?:\.\d+)?))|(?:[-+\/*()√^%])|(?:-?\.\d+))') #r'((?:-?(?:\d+(?:\.\d+)?))|(?:[-+\/*()])|(?:-?\.\d+))'
        parsed = re.findall(regex,text)
        parsed = [ float(x) if (re.match( r'(\d*\.\d+|\d+)' ,x) != None) else x for x in parsed]
        return parsed
    
    
def parse_expression(expression):

    tokens = parse_string(expression)
    tokens.append('$')

    print('--------------PARSE START - WHILE--------------')
    operationsStack = ['$']
    numbersStack = []
    print(tokens)
    while True:
        print('-----------Begin----------')
        print(tokens)

        if len(tokens) != 0:
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
                nextAction = precTable[getIndex(currentToken)][getIndex(prevOperator)]
                    
                if nextAction == 'S':
                    print('shift')
                    operationsStack.append(currentToken)
                elif nextAction == 'R':
                    print('reduce')
                    operation = operationsStack.pop()

                         
                    if currentToken == ')' and operation == ')':
                        print('insert ) back')
                        # insert back the lost ')'
                        tokens.insert(0,currentToken)

                    pushRightParenth = False
                    if operation == ')':
                        print('this')
                        pushRightParenth = True
                        if len(operationsStack) != 0:
                            operation = operationsStack.pop()

                    parseError = calculate_expression(operation,numbersStack)
                    if parseError == True:
                        return "Bad input"

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
                                
                    if operationsStack[-1] == ')' and operationsStack[-2] == '(':
                        print('pop parenth')
                        operationsStack.pop()
                        operationsStack.pop()

                        
                elif nextAction == 'ERR':
                    return "Bad input"

                elif nextAction == "A":
                    print('a')
                    print(currentToken)
                    print(tokens)
                    print(numbersStack)
                    print(operationsStack)
                    print('-----------END-----------')
                    return str(numbersStack[0])
                        
        print(numbersStack)
        print(operationsStack)    
        
