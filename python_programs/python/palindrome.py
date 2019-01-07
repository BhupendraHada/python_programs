# Problem Description: The program takes a string and checks if a string is a palindrome or not.

"""Python program to check if a string is palindrome or not. ... A string is said to be palindrome if reverse of the
string is same as string. For example, 'radar' is palindrome, but 'radix' is not palindrome."""

"""
Problem Solution
1. Take a string from the user and store it in a variable.
2. Reverse the string using string slicing and compare it back to the original string.
3. Print the final result
4. Exit.
"""


class Palindrome(object):

    def __init__(self, value):
        self.value = value

    def check_palindrome(self):
        print "reverse value", self.value[::-1]
        if self.value == self.value[::-1]:
            print "The string is a palindrome"
        else:
            print "The string isn't a palindrome"


if __name__ == "__main__":
    input = raw_input("Please enter string: ")
    p = Palindrome(input)
    p.check_palindrome()
