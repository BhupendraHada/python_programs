
class WordCount(object):

    @staticmethod
    def john_mary(str):
        john, mary = "john", "mary"
        lower_str = str.lower()
        if lower_str.count(john) == lower_str.count(mary):
            return True
        else:
            return False


print WordCount.john_mary('John&Mary')
