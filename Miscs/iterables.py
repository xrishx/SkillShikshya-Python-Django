it = iter([1,2,3, 4, 5])
print (next(it))
while True:
    try:
        no = next(it)
        print (no)
    except StopIteration:
        break

### ------------------------------------------------ ###

class Oddnumbers:

    def __init__(self, end_range):
        self.start = -1
        self.end = end_range

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end-1:
            self.start += 2
            return self.start
        else:
            raise StopIteration

countiter = Oddnumbers(10)
while True:
    try:
        no = next(countiter)
        print (no)
    except StopIteration:
        break