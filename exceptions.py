def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    except NameError:
        print('I catch you')
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

def divide2(x, y):
    try:
        for i in range(1, x):
            for j in range(1, y):
                if i // j == 1:
                    raise NameError("what the hell")
    except NameError:
        print('I catch you')




divide2(2, 2)
divide2(2, 0)
divide2("2", "1")

divide(2, 1)
divide(2, 0)
divide("2", "1")
