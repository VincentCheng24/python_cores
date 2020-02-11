import functools


# Note:  examples
def upperCase(func):
    def warper():
        ori_res = func()
        new_res = ori_res.upper()
        return new_res

    return warper


def greet():
    return 'Hello World'


@upperCase
def upperGreet():
    return 'Hello World'


print(greet())
print(upperGreet())

# these are two func obj, the second is the wrapper which calls the decorated func
print(upperGreet)
print(upperCase(upperGreet))


# multiple decorator to one function
def strong(func):
    def warpper():
        return '<strong>' + func() + '</strong>'

    return warpper


def loud(func):
    def wrapper():
        return '<loud>' + func() + '</loud>'

    return wrapper


@strong
@loud
def xmlGreet():
    return 'hell'


def xml_greet():
    return 'go'


print(xmlGreet())
print(strong(loud(xml_greet())), '\n')


# decorated function with input args

def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'trace calls {func.__name__}() with arg {args}, {kwargs}')

        ori_res = func(*args, **kwargs)

        print(f'trace: {func.__name__}() returns {ori_res!r}')

        return ori_res

    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


say('Jane', 'Hello, World')


# Note: applications

# Define a class with a singleton instance.
def singleton(cls):
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance


@singleton
class MyClass:
    ...


# Add attributes to a function.
def attrs(**kwds):
    def decorate(f):
        for k in kwds:
            setattr(f, k, kwds[k])
        return f

    return decorate


@attrs(versionadded="0.0", author="Vincent")
def example():
    print('test')


# Counting Recursive Function Calls with Decorators
def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0

    return helper


@call_counter
def for_loop(n):
    for i in range(n):
        print(i)


@call_counter
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(for_loop(100), for_loop.calls)
print(fib(10), fib.calls)



# python built-int decorators
class DecoratorTest(object):
    """
    Test regular method vs @classmethod vs @staticmethod
    """

    def __init__(self):
        """Constructor"""
        pass

    def doubler(self, x):
        """"""
        print("running doubler")
        return x*2

    @classmethod
    def class_tripler(klass, x):
        """"""
        print("running tripler: %s" % klass)
        return x*3

    @staticmethod
    def static_quad(x):
        """"""
        print("running quad")
        return x*4


class Fees(object):

    def __init__(self):
        self._fee = None

    @property
    def fee(self):
        return self._fee

    @fee.setter
    def set_fee(self, fee):
        self._fee = fee

    # fee = property(get_fee, set_fee)


if __name__ == "__main__":
    decor = DecoratorTest()
    print(decor.doubler(5))
    print(decor.class_tripler(3))
    print(DecoratorTest.class_tripler(3))
    print(DecoratorTest.static_quad(2))
    print(decor.static_quad(3))

    print(decor.doubler)
    print(decor.class_tripler)
    print(decor.static_quad)