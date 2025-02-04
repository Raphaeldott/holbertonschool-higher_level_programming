#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle


try:
    r2 = Rectangle(2000000000000000000, 1)

except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
