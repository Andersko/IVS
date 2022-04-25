"""!
Module for expression parser logic

@file expression_parser.py
@author Adam Kostolányi
@date 11.4.2022
"""

import re
import my_math

"""!
Precedence table for operations
"""
precTable = [
    # prev +-     *,/    (      )      !      ^      √      %      $    # current
    ['R', 'R', 'S', 'R', 'R', 'R', 'ERR', 'ERR', 'S'],  # +-
    ['S', 'R', 'S', 'R', 'R', 'R', 'ERR', 'ERR', 'S'],  # */
    ['S', 'S', 'S', 'ERR', 'R', 'S', 'S', 'ERR', 'S'],  # (
    ['R', 'R', 'P', 'R', 'R', 'R', 'R', 'ERR', 'S'],  # )
    ['S', 'S', 'S', 'R', 'R', 'R', 'ERR', 'ERR', 'S'],  # !
    ['S', 'S', 'S', 'R', 'R', 'S', 'ERR', 'ERR', 'S'],  # ^
    ['S', 'S', 'S', 'R', 'ERR', 'S', 'ERR', 'ERR', 'S'],  # √
    ['ERR', 'ERR', 'ERR', 'R', 'ERR', 'ERR', 'ERR', 'ERR', 'S'],  # %
    ['R', 'R', 'ERR', 'R', 'R', 'R', 'R', 'R', 'A'],  # $
]


def getIndex(operator):
    """!
    Get index of the given operator for precedence table

    @param operator Operator we want to get index of
    @return Index of the operator for precedence table
    """
    if operator == '+' or operator == '-':
        return 0
    elif operator == '*' or operator == '/':
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


def calculate_expression(operation, numberList):
    """!
    Calculate the expression of the highest precedence

    @param operation Operation of the current expression
    @param numberList Stack with the expression constants
    @return True if expression has incorrect input
    """
    result = 0.0
    if operation == '+':
        if len(numberList) >= 2:
            last = numberList.pop()
            preLast = numberList.pop()
            result = my_math.add(preLast, last)
        else:
            return True
    elif operation == '-':
        if len(numberList) >= 2:
            last = numberList.pop()
            preLast = numberList.pop()
            result = my_math.subtract(preLast, last)
        else:
            return True
    elif operation == '*':
        if len(numberList) >= 2:
            last = numberList.pop()
            preLast = numberList.pop()
            result = my_math.multiply(preLast, last)
        else:
            return True
    elif operation == '/':
        if len(numberList) >= 2:
            last = numberList.pop()
            preLast = numberList.pop()
            result = my_math.divide(preLast, last)
        else:
            return True
    elif operation == '!':
        if len(numberList) >= 1:
            last = numberList.pop()
            result = my_math.factorial(last)
        else:
            return True
    elif operation == '^':
        if len(numberList) >= 2:
            last = numberList.pop()
            preLast = numberList.pop()
            result = my_math.power(preLast, last)
        else:
            return True
    elif operation == '√':
        if len(numberList) >= 1:
            last = numberList.pop()
            preLast = numberList.pop()
            result = my_math.root(last, preLast)
        else:
            return True
    elif operation == '%':
        if len(numberList) >= 2:
            last = numberList.pop()
            preLast = numberList.pop()
            result = my_math.modulo(preLast, last)
        else:
            return True

    numberList.append(result)
    return False


def parse_string(text):
    """!
    Parses the expression into array of the given string

    @param text String to parse into expression
    @return Parsed expression
    """
    regex = re.compile(
        r'((?:(?<!\d)[\+\-]?(?:\d+(?:\.\d+)?))|(?:[\!\-\+\/\*\(\)\√\^\%]))'
    )
    parsed = re.findall(regex, text)
    parsed = [
        float(x) if (re.match(r'([\+\-]?(?:\d*\.\d+|\d+))', x) != None) else x
        for x in parsed
    ]
    return parsed


def parse_expression(expression):
    """!
    Parses the given string into expressions and calculates it

    @param expression Expression to parse and calculate
    @return Return either the result nor string 'Bad input'
    """
    tokens = parse_string(expression)
    tokens.append('$')

    operationsStack = ['$']
    numbersStack = []

    while True:

        if len(tokens) != 0:
            currentToken = tokens.pop(0)

        if isinstance(currentToken, float):
            # If current token is a number, push it to the number stack
            numbersStack.append(currentToken)
        elif isinstance(currentToken, str):
            # If current token is a operator

            if operationsStack[-1] == '$' and len(tokens) != 0:
                # If we got first operation from expression
                operationsStack.append(currentToken)
            else:

                previousOperator = operationsStack[-1]
                nextAction = precTable[getIndex(currentToken)][
                    getIndex(previousOperator)
                ]

                if nextAction == 'S':
                    # If next action is shift
                    operationsStack.append(currentToken)
                elif nextAction == 'R':
                    # If next action is reduce expression

                    operation = operationsStack.pop()

                    if currentToken == ')' and operation == ')':
                        # insert back the lost ')'
                        tokens.insert(0, currentToken)

                    pushRightParenthesisBack = False
                    if operation == ')':
                        pushRightParenthesisBack = True
                        if len(operationsStack) != 0:
                            operation = operationsStack.pop()

                    parseError = calculate_expression(operation, numbersStack)
                    if parseError == True:
                        return 'Bad input'

                    if currentToken != '$':
                        # Push back the 'ignored' token
                        operationsStack.append(currentToken)
                    else:
                        tokens.insert(0, currentToken)

                        if pushRightParenthesisBack:
                            # Pushing back the rigth parenthesis after calculating the expression
                            operationsStack.append(')')
                            if len(operationsStack) < 2:
                                return 'Bad input'

                    if operationsStack[-1] == ')' and operationsStack[-2] == '(':
                        # Pop parentheses if there are no operations inbetween
                        operationsStack.pop()
                        operationsStack.pop()

                elif nextAction == 'P':
                    if operationsStack[-1] == '(' and currentToken == ')':
                        operationsStack.pop()

                elif nextAction == 'ERR':
                    return 'Bad input'

                elif nextAction == 'A':
                    # Parsing finished
                    if len(numbersStack) != 1:
                        return 'Bad input'

                    return str(numbersStack[0])
