#!/usr/bin/python3
"""
    Prints text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
"""


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
    temp_text = ""

    for c in text:
        temp_text += c
        if c in chars:
            print(temp_text.strip(), end="\n\n")  # Print without spaces trail
            temp_text = ""  # Reset the temporary text
        elif temp_text == " ":
            temp_text = ""  # Remove leading spaces after punctuation

    # Print remaining text without adding extra newlines
    if temp_text.strip():
        print(temp_text.strip(), end="")  # Remove extra spaces and new line
