# class-based iterator
class Reverse():

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


# generator
def revGenerator(data):

    for i in range(len(data)-1, -1, -1):
        yield data[i]


# generator expression
print(sum(x*x for x in range(10)))
print(max(x*y for x, y in zip([4,7,3], [10, 23, 56])))

res = Reverse([1, 2, 4, 5])

for v in res:
    print(v)

for v in revGenerator('Hello World'):
    print(v)