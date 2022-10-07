class GreatNumerator:
    def __init__(self, lists):
        self.lists = lists
    
    def __iter__(self):
        self.c = 0
        return self      
       
    def __next__(self):
        if self.c < len(self.lists):
            s = str(self.c) + ' ' + self.lists[self.c]
            self.c += 1
            return s
        else:
            raise StopIteration


lists = ['111', 'cat', 'got', 'ddd', '222']
t = GreatNumerator(lists)
for i in t:
    # temp = t.__iter__()
    # n = temp.__next__()
    # del temp
    print(i)
