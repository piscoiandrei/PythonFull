# OTHER TIPS AND TRCIKS
# TODO ACTUAL COPYING aka DEEPCOPY
"""
import copy

obj1 = SomeOject
cpy = copy.deepcopy(obj1)  # used for nested stuff or normal
# copy.deepcopy() can be used on any object

"""


def gen(n):
    print('beginning of func')
    while n > 0:
        print(f'before yield, n is {n}')
        yield n
        n -= 1
        print(f'after expression, n is {n}')

    print('outside while/ end ----')


mg = gen(4)
ok = True
while ok:
    try:
        next(mg)
    except StopIteration:
        ok = False
        print('STOP ITERATION EXCEPTION')


