class Pagination:
    def __init__(self, items=None, pageSize=10):
        if items is None:
            items = []
        self.items = items
        self.pageSize = pageSize

    def getVisibleItems(self):
         self.pageSize



alphabetList = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()

p = Pagination(alphabetList, 4)
print(p.items)
print(p.getVisibleItems())
