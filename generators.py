# generates a value one at a time using lazy iterators, its memory optimal,
# used for working with big data sets
# Generator = memory eficient iterable

def countdown(num):
    print('Starting')
    while num > 0:
        yield num  # returns num and remembers the state of the function so
        # when called again it will iterate after the yield statement
        num -= 1


cd = countdown(4)
val = next(cd)
print(val)
print(next(cd))
print(next(cd))
print(next(cd))


def inf_sequence_gen():
    num = 0
    while True:
        yield num
        num += 1


my_generator = (i for i in range(13) if i % 2 == 0)  # use '( )' not '[ ]'
