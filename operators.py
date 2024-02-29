#!/usr/bin/python3

import operator

OPS = {
    '+': (1, operator.add),
    '-': (1, operator.sub),
    '*': (2, operator.mul),
    '/': (2, operator.truediv),
    '%': (2, operator.mod)
}

"""
This module defines a dictionary containing basic arithmetic operators mapped to their precedence and corresponding functions.
"""

# Define operators and their precedence
