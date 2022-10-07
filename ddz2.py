class GreatNumerator:
    def __init__(self, lists):
        self.lists = lists
    def __iter__(self):
        return IteratorOfGreatNumerator(self.lists)
        
class IteratorOfGreatNumerator:
    def __init__(self, lists):
        self.l = lists.copy()
        self.c = 0
        
    def __next__(self):
        if self.c < len(self.l):
            s = str(self.c) + ' ' + self.l[self.c]
            self.c += 1
            return s
        else:
            raise StopIteration


lists = ['111', 'cat', 'got', 'ddd', '222']
t = GreatNumerator(lists)
for i in t:
    print(i)
