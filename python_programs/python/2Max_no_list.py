# a = [3, 5, 2, 6, 9, 44, 56, 23, 56
#      ]
#
# result = []
# count = 0
#
# for i in a:
#     max_value = max(a)
#     print max_value
#     if max_value not in result:
#         result.append(max_value)
#         count += 1
#     print count
#     if count >= 2:
#         break
#     a.remove(max_value)
#
# print "result", result

########################
numbers = [20, 67, 3, 2.6, 7, 74, 2.8, 90, 90, 52.8, 4, 3, 2, 5, 7]

# if numbers[0] > numbers[1]:
#     m, m2 = numbers[0], numbers[1]
# else:
#     m, m2 = numbers[1], numbers[0]
#
# for x in numbers[2:]:
#     if x > m2:
#         if x > m:
#             m2, m = m, x
#         else:
#             m2 = x
#
# print m2

############################# removing duplicate case
def second_largest(numbers):
    first, second = None, None
    for n in numbers:
        if n > first:
            first, second = n, first
        elif n > second:
            second = n
    return second


result = second_largest(numbers)
print result


######### Using Sorting
l = [19, 1, 2, 3, 4, 20, 20]
sorted(set(l))[-2]


# Python program to find largest, smallest,
# second largest and second smallest in a
# list with complexity O(n)

def get_numbers(list1):
    largest = list1[0]
    largest2 = list1[0]
    lowest = list1[0]
    lowest2 = list1[0]
    for item in list1:
        if item > largest:
            largest = item
        elif largest2 != largest and largest2 < item:
            largest2 = item
        elif item < lowest:
            lowest = item
        elif lowest2 != lowest and lowest2 > item:
            lowest2 = item

    print("Largest element is:", largest)
    print("Smallest element is:", lowest)
    print("Second Largest element is:", largest2)
    print("Second Smallest element is:", lowest2)


# Driver Code
list1 = [12, 45, 2, 41, 31, 10, 8, 6, 4]
get_numbers(list1)
