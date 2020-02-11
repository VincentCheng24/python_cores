# nested func
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)

    data_transmitter()


transmit_to_space("Test message")
print(transmit_to_space("Test message"))


# nested func with 'nonlocal' keyword which enables the modification of local variables
def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number = 3
        print(number)
    printer()
    print(number)

print_msg(9)


# closure
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
    return data_transmitter


fun2 = transmit_to_space("Burn the Sun!")
fun2()


# exercise
def multiplier_of(num):
    def multi(x):
        return x * num
    return multi

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))
multiplywith10 = multiplier_of(10)
print(multiplywith10(9))