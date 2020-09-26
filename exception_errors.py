def func1(x):
    if x < 0:
        raise Exception("X should be positive")


def func2(x):
    assert (x >= 0), 'x is not positive'


def raise_excep():
    raise Exception("Atentie jonule ca te vaneaza dorian popa")


def func3(a, b):
    try:
        a = a / b
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)
    else:
        print("everything is ok")
    finally:  # executes everytime
        print("finnaly block executed")

#  You can also define exeptions but at the time this is being created it's
#  not the case yet
