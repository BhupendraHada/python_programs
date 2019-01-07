
class MovingTotal:

    def __init__(self):
        self.numbers = []

    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        self.numbers.extend(numbers)
        self.num_totals = []
        for i in range(0, len(self.numbers) - 2):
            num_list = self.numbers[i:i + 3]
            num_sum = sum(num_list)
            self.num_totals.append(num_sum)

    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        if total in self.num_totals:
            return True
        else:
            return False


movingtotal = MovingTotal()
movingtotal.append([1, 2, 3])
print(movingtotal.contains(6))
movingtotal.append([4])
print(movingtotal.contains(9))
print(movingtotal.contains(7))

