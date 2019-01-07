class CategoryTree:

    def __init__(self):
        self.category = {}

    def add_category(self, category, parent):

        if parent:
            try:
                self.category[parent]
                childs = self.category.get(parent)
                try:
                    if str(category) in childs:
                        raise KeyError('Child Category already exist.')
                except KeyError as e:
                    print (e)
                else:
                    self.category[parent].append(category)
            except KeyError as e:
                print (e.__str__())
        else:
            try:
                self.category[category]
            except KeyError as e:
                self.category[category] = []

    def get_children(self, parent):
        return self.category.get(parent)


c = CategoryTree()
c.add_category('A', None)
c.add_category('B', 'A')
c.add_category('C', 'A')
print(','.join(c.get_children('A') or []))
