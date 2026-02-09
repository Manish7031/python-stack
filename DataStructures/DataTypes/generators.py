## generators

import sys

class  Iter:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        self.current += 1

        if self.current >= self.n:
            raise StopIteration
        return self.current
    
    def gen(n):
        for i in range(n):
            yield i


# for i in Iter.gen(10):
#     print(i)
x= Iter.gen(10)
print(next(x))
print(next(x))
print(next(x))
print(next(x))