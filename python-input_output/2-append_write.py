#!/usr/bin/python3
'''
def to append
'''


def append_write(filename="", text=""):
    '''
    append in a file
    '''
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
