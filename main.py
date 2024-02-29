#!/usr/bin/python3
import sys
from evaluator import evaluate_expression

"""
This script evaluates an arithmetic expression provided
as a command-line argument.
"""

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:", sys.argv[0], "<expression>")
        sys.exit(1)

    result = evaluate_expression(sys.argv[1])
    if result is not None:
        print("Result:", result)