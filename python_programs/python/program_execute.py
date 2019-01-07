import itertools

class Program(object):
    a = [2, 56, 35, 6, 34, 76, 23, 2, 75, 2, 75]

    def get_duplicate(self):
        # Find out duplicate in list
        seen = {}
        duplicate = []
        for i in self.a:
            if i not in seen:
                seen[i] = 1
            else:
                if seen[i] == 1:
                    duplicate.append(i)
                seen[i] += 1
        print "duplicates: ", duplicate

    def get_second_highest(self):
        max1 = max2 = 0
        for i in self.a:
            if i > max1:
                max2 = max1
                max1 = i
            elif i > max2 and max1 != i:
                max2 = i
        print "Max1 {} and max2 {}".format(max1, max2)

    def get_count(self):
        # Find out count of elements in list
        seen = {}
        for i in self.a:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
        print "List elements Count: ", seen

    def get_unique(self):
        # Find out unique elements in list
        uniq = []
        for i in self.a:
            if i not in uniq:
                uniq.append(i)
        print "Unique elements in list: ", uniq

    def sort_list(self):
        # Sort list with out in build functions
        # new_list = []
        # while self.a:
        #     minimum = self.a[0]  # arbitrary number in list
        #     for x in self.a:
        #         if x < minimum:
        #             minimum = x
        #     new_list.append(minimum)
        #     self.a.remove(minimum)
        # print "Sorted List: ", new_list
        l = self.a
        for i in range(len(self.a)):
            for j in range(i + 1, len(self.a)):
                if l[i] > l[j]:
                    l[i], l[j] = l[j], l[i]
        print "Sorted List: ", l

    def odd_string_change(self):
        input = 'aabbbxxxxyzzzzz'
        import re

        N = "wherewhere"
        cnt = 0
        result = ''
        countN = 0
        showresult = []

        for i in range( 1, len(N) + 1):
            if cnt <= len(re.findall(N[0:i], N)):
                cnt = len(re.findall(N[0:i], N))
                result = re.findall(N[0:i], N)[0]
                countN = len(N) / len(result)
        for i in range(0, countN):
            showresult.append(result)
        print showresult
        # from itertools import groupby
        # result = [''.join(list(group)) for key, group in groupby(input)]
        # print "result", result
        # input_list = []
        # output = ''
        # for val in result:
        #     if len(val) > 1 and len(val) % 2 != 0:
        #         output += val[0]
        #     else:
        #         output += val
        # print output

    def prog(self):
        def yrange(n):
            i = 0
            while i < n:
                yield i
                i += i

        A = lambda x: 'Hello' if x ** x == x else 'Hi'
        B = lambda x: 'Jaya' if x ** x == 1 else 'Hema'
        y = yrange(4)
        print A(int(y.next()))
        print B(int(y.next()))

    def ex(self):
        lo = 2
        hi = 10


if __name__ == '__main__':
    p = Program()
    print "List elements: ", p.a
    p.get_duplicate()
    p.get_second_highest()
    p.get_count()
    p.get_unique()
    p.sort_list()
    p.odd_string_change()
    p.prog()
    p.ex()
