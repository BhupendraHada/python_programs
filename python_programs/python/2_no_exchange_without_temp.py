# -*- coding: utf-8 -*-

"""
Problem Description:
The program takes both the values from the user and swaps them without using temporary variable.
"""

a=int(input("Enter value of first variable: "))
b=int(input("Enter value of second variable: "))
a=a+b
b=a-b
a=a-b
print("a is:", a, " b is:", b)
