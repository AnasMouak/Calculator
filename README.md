# Calculator

A simple command-line calculator program written in Python.

## Overview

This calculator program evaluates arithmetic expressions entered as command-line arguments. It supports basic arithmetic operations such as addition, subtraction, multiplication, and division. Additionally, it handles parentheses for controlling operator precedence and prints error messages for invalid expressions or operators.

## Usage

To use the calculator, run the `main.py` script with an arithmetic expression as an argument. For example:
```bash
$ ./main.py 2.3*2+2
Result: 6.6
$ ./main.py 3*4/2
Result: 6.0
$ ./main.py 1-2*3
Result: -5.0
```

## Error Handling
The calculator program provides informative error messages for invalid expressions or operators. Here are some examples:

# Invalid operator =

```bash
$ ./main.py "2.3*2=2"
Error: Invalid operator =
```

# Invalid operator p
```bash
$ ./main.py "2.3*2p2"
Error: Invalid operator p
```
In both cases, the calculator detects the invalid operators (= and p) and prints an error message indicating the issue.

## Features

Parses and evaluates arithmetic expressions accurately.
Supports the following arithmetic operations:
Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
Handles parentheses to enforce operator precedence.
Provides clear error messages for invalid expressions or operators.

## File Structure

The project is organized as follows:

main.py: Main entry point of the calculator program.
evaluator.py: Contains the logic for parsing and evaluating arithmetic expressions.
stack.py: Defines a stack data structure used in the evaluation process.
operators.py: Defines the supported operators and their precedence.
utils.py: Contains utility functions used throughout the project.

## Installation

No installation is required. Simply clone the repository to your local machine to start using the calculator.

```bash
git clone https://github.com/your-username/calculator.git
cd calculator
```