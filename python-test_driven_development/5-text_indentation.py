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
    temp_text = ""
    for c in text:
        temp_text += c
        if c in chars:
            temp_text = temp_text.strip()  # Remove any trailing spaces
            print(temp_text)
            print()  # Print a blank line
            temp_text = ""  # Reset temp_text for the next part

    # For the remaining part of the text after the last punctuation
    if temp_text:
        print(temp_text.strip())  # Ensure no trailing spaces before printing
