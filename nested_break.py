import numpy as np

# very elegant !!!!
for a in range(1, 5):
    for b in range(1, 3):
        if a // b == 2:
            # Break the inner loop...
            break
    else:
        # Continue if the inner loop wasn't broken.
        continue
    # Inner loop was broken, break the outer.
    break


# option 2
try:
    for a in range(3):
        for b in range(3):
            if a==b==1:
                raise StopIteration
            print(b)
except StopIteration:
    pass


# make a function, using return/ yield to stop the execution
def myfunc():
    for i in range(1, 1001):
        for i2 in range(i, 1001):
            for i3 in range(i2, 1001):
                if i*i + i2*i2 == i3*i3 and i + i2 + i3 == 1000:
                    print(i*i2*i3)
                    return # Exit the function (and stop all of the loops)
                    # or yield i*i2*i3


myfunc() # Call the function