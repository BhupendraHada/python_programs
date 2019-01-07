# Simple Try-Except

"""
finally is executed regardless of whether the statements in the try block fail or succeed. else is executed only
if the statements in the try block don't raise an exception and don't use any keywords like break, continue, return etc.
"""


def fun():
    try:
        print 1
        2/0
        return "Try"
    except:
        print "error"
    else:
        print "else"
    finally:
        print "finally"
        return "finally"
        """a return here will hijack the return functionality. None of the above return works. Only finally return will
        execute."""


result = fun()
print result

try:
    print 1
finally:
    print "finally"

# Defult except must be last.
try:
    print 1
except ZeroDivisionError as e:
    print "error1"
except:
    print "error2"
