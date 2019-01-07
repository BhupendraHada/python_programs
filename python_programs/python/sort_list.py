# Different techniques to sort a given list

a = [3, 2, 5, 4, 2, 1, 7, 9, 1, 11, 9]
#
# sort_list = []
# for i in range(len(a)):
#     min_val = a[0]
#     print "min_valstart ", min_val
#     for val in a:
#         if val < min_val:
#             min_val = val
#     print min_val
#     a.remove(min_val)
#     sort_list.append(min_val)

# Using range and for loop
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]
#
# print "sort_list", a


# Using Min function
# sort_list = []
#
# for i in range(len(a)):
#     min_val = min(a)
#     sort_list.append(min_val)
#     a.remove(min_val)
# print sort_list


sort_list = []
for i in range(len(a)):
    min_val = a[0]
    min_index = 0
    for val in a:
        if val < min_val:
            min_val = val
            min_index = a.index(min_val)
    del a[min_index]
    sort_list += [min_val]

print "sssssss", sort_list


a.sort() # sort a given list

sorted_list = sorted(a) # sort a list and return a new list
