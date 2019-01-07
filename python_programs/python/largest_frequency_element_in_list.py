# Method #1 : Naive method

#using naive method to
# get most frequent element
test_list = [9, 4, 5, 4, 4, 5, 9, 5, 4]

max = 0
res = test_list[0]
for i in test_list:
    freq = test_list.count(i)
    if freq > max:
        max = freq
        res = i

# Method #2 : Using max() + set()
res = max(set(test_list), key = test_list.count)

#Method #3 : Using collections.Counter.most_common()
test_list = Counter(test_list)
res = test_list.most_common(1)[0][0]
