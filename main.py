from my_decorators.my_wrappers import *


@timer
@debug
def some_function(x):
    k = 0
    for i in range(5, x):
        k += ((i / (i + 1) - i / i + i + i - i / (i - 1)) * 0.000003) * i
    return k


print(some_function(10))
