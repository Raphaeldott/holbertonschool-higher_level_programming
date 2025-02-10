#!/usr/bin/python3
'''
write in a file
'''


def write_file(filename="", text=""):
    '''
    writing inside a file
    '''
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
