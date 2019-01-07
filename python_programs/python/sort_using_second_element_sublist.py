from sort_dict import DATA

# # Method 1: Using the Bubble Sort technique
#
#
# # Python code to sort the lists using the second element of sublists
# # Inplace way to sort, use of third variable
# def sort_func(sub_li):
#     l = len(sub_li)
#     for i in range(0, l):
#         for j in range(0, l - i - 1):
#             if sub_li[j][1] > sub_li[j + 1][1]:
#                 tempo = sub_li[j]
#                 sub_li[j] = sub_li[j + 1]
#                 sub_li[j + 1] = tempo
#     return sub_li
#
#
# # Driver Code
# sub_li = [['rishav', 10], ['akash', 5], ['ram', 20], ['gaurav', 15]]
# print(sort_func(sub_li))
#
#
# # Method 2: Sorting by the use of sort() method
#
# sub_li.sort(key=lambda x: x[1])
#
#
# # Method 3: Sorting by the use of sorted() method
# sorted(sub_li, key = lambda x: x[1])

#
sub_li = [[1234, 'rishav', 1],
          [234, 'akash', 5],
          [134, 'ram', 20],
          [1234, 'rishav', 1],
          [124, 'gaurav', 1],
          [124, 'gaurav', 1],
          [1234, 'rishav', 1]]

tup_li = [tuple(t) for t in sub_li]
print tup_li

result = {}

for tp in tup_li:
    if tp not in result:
        result[tp] = 1
    else:
        result[tp] += 1

print result

#  Ways to sort list of dictionaries by values in Python Using lambda function
#Using lambda functions
#Using itemgetter

lis = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

print sorted(lis, key=lambda i: i['age'])

# by both age and name.
print sorted(lis, key=lambda i: (i['age'], i['name']))

# by age in descending order
print sorted(lis, key=lambda i: i['age'], reverse=True)

print DATA
