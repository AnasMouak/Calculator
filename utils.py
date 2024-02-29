#!/usr/bin/python3

def is_float(s):
    """
    Check if a string can be converted to a float.

    Parameters:
    s (str): The input string to check.

    Returns:
    bool:True if the input string can be converted to a float, False otherwise.
    """
    try:
        float(s)
        return True
    except ValueError:
        return False