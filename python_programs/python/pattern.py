"""
python pattern programs.
"""

# for r in range(1,5):
#     for c in range(1, r+1):
#         print c,
#     print
#
#
#
# for i in range(10):
#     print "using join ", (' '.join([str(n) for n in range(0, i)]))
#     print i,
#
#
# ######### Simple pyramid pattern
# num =3
# j = num
# for i in range(0, num + 1):
#     print('{}{}'.format(' ' * j, ' *' * i))
#     j -= 1
#
# ######### left pentagon
# num =3
# j = num
# for i in range(0, num + 1):
#     print '{}'.format('* ' * i)
#     j -= 1

######### right pentagon
# num =3
# j = num
# for i in range(1, num + 1):
#     print '{}{}'.format(' ' * (num -i), '*' * i)
#     # j -= 1

#
# # After 180 degree rotation
# def pypart2(n):
#     # number of spaces
#     k = 2 * n - 2
#
#     # outer loop to handle number of rows
#     for i in range(0, n):
#
#         # inner loop to handle number spaces
#         # values changing acc. to requirement
#         for j in range(0, k):
#             print " ",
#
#             # decrementing k after each loop
#         k = k - 2
#
#         # inner loop to handle number of columns
#         # values changing acc. to outer loop
#         for j in range(0, i + 1):
#             # printing stars
#             print "* " * j
#
#             # ending line after each row
#
#     # Driver Code
#
#
# n = 5
# pypart2(n)

# 1)
"""
* * * * * * 
* * * * * 
* * * * 
* * * 
* *
*
"""
# rows = 5
# for i in range(rows, 0,-1):
#     for j in range(0, i):
#         print "*",
#     print


# 2)
"""
* 
* * 
* * * 
* * * * 
* * * 
* * 
*
"""
#
# rows = 5
# for i in range(0, rows):
#     for j in range(0, i):
#         print "*",
#     print
# for i in range(rows, 0, -1):
#     for j in range(0, i):
#         print"*",
#     print


"""
0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1
0
"""

#
# rows = 5
# for i in range(rows, 0, -1):
#     for j in range(0, i):
#         print j,
#     print


"""

* * * * 
* * * 
* * 
*
* 
* * 
* * * 
"""

rows = 5

for i in range(rows, 0, -1):
    for j in range(0, i):
        print"*",
    else:
        if i == 1:
            print "",
        else:
            print
for i in range(0, rows+1):
    for j in range(0, i):
        print "*",
    print

