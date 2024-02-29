#!/usr/bin/python3

from stack import Stack
from operators import OPS
from utils import is_float



def evaluate_expression_logic(expression, operand_stack, operator_stack):
    """
    Evaluate arithmetic expression logic.

    Args:
        expression (str): The arithmetic expression.
        operand_stack (Stack): Stack to store operands.
        operator_stack (Stack): Stack to store operators.

    Returns:
        float or None: The result of the arithmetic expression evaluation.
    """
    i = 0
    while i < len(expression):
        if expression[i].isdigit() or (expression[i] == '.' and 
                                       i + 1 < len(expression) and 
                                            expression[i + 1].isdigit()):
            # Extract the operand
            j = i
            while j < len(expression) and (expression[j].isdigit() 
                                           or expression[j] == '.'):
                j += 1
            operand = float(expression[i:j])
            operand_stack.push(operand)
            i = j - 1  # Move i to the last digit of the operand
        elif expression[i] in OPS:
            # Process operators
            op = expression[i]
            while operator_stack and OPS.get(operator_stack.peek(), 
                                             (0, None))[0] >= OPS.get(op, 
                                                                      (0, 
                                                                       None
                                                                       ))[0]:
                b = operand_stack.pop()
                a = operand_stack.pop()
                operator = operator_stack.pop()
                operand_stack.push(OPS[operator][1](a, b))
            operator_stack.push(op)
        elif expression[i] == '(':
            # Push '(' onto the operator stack
            operator_stack.push('(')
        elif expression[i] == ')':
            # Evaluate expression until '(' is encountered
            while operator_stack.peek() != '(':
                b = operand_stack.pop()
                a = operand_stack.pop()
                operator = operator_stack.pop()
                operand_stack.push(OPS[operator][1](a, b))
            # Pop '(' from the operator stack
            operator_stack.pop()
        elif expression[i] not in OPS and expression[i] not in '()':
            print("Error: Invalid operator", expression[i])
            return None
        i += 1

    # Evaluate remaining operators
    while not operator_stack.is_empty():
        b = operand_stack.pop()
        a = operand_stack.pop()
        operator = operator_stack.pop()
        operand_stack.push(OPS[operator][1](a, b))

    return operand_stack.peek()

def evaluate_expression(expression):
    """
    Evaluate arithmetic expression.

    Args:
        expression (str): The arithmetic expression.

    Returns:
        float or None: The result of the arithmetic expression evaluation.
    """
    operand_stack = Stack()
    operator_stack = Stack()

    result = evaluate_expression_logic(expression, operand_stack, 
                                       operator_stack)
    return result