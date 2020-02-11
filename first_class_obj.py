# a normal function
def yell(text):
    return text.upper() + '!'


print(yell('hello'))

# assignment
scream = yell
print(scream('what the hell'))

# function obj and func name are two separate pieces
# del yell
# print(yell('really')) # NameError: name 'yell' is not defined
print(scream('try again'))
print(scream.__name__) # the name of a func is defined on creation

# func can be obj stored in data structures
funcs = [scream, yell, str.upper, str.lower]
print(funcs[1]('can be aCCessed this way'))
for f in funcs:
    print(f, f('hey there'))


# func can be passed to other functions (high-order functions)
def greet(func):
    print(func('this is How it works'))


greet(yell)
greet(scream)
greet(funcs[-1])


# func can be nested
def speak(text):
    def whisper(t):
        t += 'hello'
        return t.lower() + '...'
    return whisper(text)


print(speak('NEsted Func'))

# inner func can't be accessed outside
# whisper('hello')


# but you can access the inner func if the parent func can return the inner func as an obj
def get_speak_func(th):
    def whisper(text):
        return text.lower() + '$$$'

    def yell(text):
        return text.upper() + '@@@'

    if th > 0.5:
        return yell
    else:
        return whisper


call = get_speak_func(0.8)
print(call('Hello World'))


# func can capture local state
def get_speak(t, th):
    def whisper():
        return t.lower()

    def yell():
        return t.upper()
    if th > 0.5:
        return yell
    else:
        return whisper


print(get_speak('heLlo again', 0.7)())


# another e.g.
def set_adder(n):
    def adder(x):
        return x + n
    return adder


add_3 = set_adder(3)
add_10 = set_adder(10)
print(add_3(7))
print(add_10(7))


# obj can behave like func

class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return x + self.n


add_5 = Adder(5)
print(add_5(15))

# check the callability
print(callable(add_5))
print(callable(Adder))
add = 5
print(callable(add))