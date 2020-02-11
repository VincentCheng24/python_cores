def print_vars(arg1, *args, **kwargs):

    print('arg1:', arg1)

    print(type(args))
    for arg in args:
        print(arg)

    print(type(kwargs))
    for key, arg in kwargs.items():
        print(key, arg)


print_vars('one', 'two', 'whar', name='neo', phone='iphone')


def multiplication(*args):
    if len(args) == 0:
        return 0

    product = 1
    for arg in args:
        product *= arg

    return product


print(multiplication(11, 9, 22, 55, 10))
print(multiplication(11, 9, 22, 55, -100, 0.0003))