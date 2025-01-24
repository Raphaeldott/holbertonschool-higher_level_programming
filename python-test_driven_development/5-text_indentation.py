#!/usr/bin/python3
def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ['.', '?', ':']
    result = ""
    for c in text:
        result += c
        if c in chars:
            result += "\n\n"
    lines = result.split('\n')
    for line in lines:
        print(line.strip())
