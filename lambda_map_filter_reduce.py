from functools import reduce


# lambda
add = lambda x, y: x + y
print(add(4, 6))

a = [(1, 2), (4, 1), (9, 10), (13, -3)]
sorted_a = sorted(a, key=lambda x: x[1])
a.sort(key=lambda x: x[1])
print(sorted_a)

# map
lis = [1, 2, 3, 4, 5]
res = list(map(lambda x: x**2, lis))
print(res)

sub = lambda x: x - x
add = lambda x: x + x

for i in range(5):
    val = list(map(lambda x: x(i), [add, sub]))
    print(val)

# filter
res2 = list(filter(lambda x: x % 2 == 0, lis))
print(res2)

lis3 = range(-5, 5)
res3 = list(filter(lambda x: x < 0, lis3))
print(res3)

# reduce
Sum = reduce(lambda x, y: x + y, lis)
print(Sum)

product = reduce(lambda x, y: x * y, lis)
print(product)


print('well done')