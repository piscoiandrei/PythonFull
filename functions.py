def foo(*args, **kwargs):
    # args = tuple
    for arg in args:
        print(arg)

    # kwargs = dictionary
    for key in kwargs:
        print(key, kwargs[key])


def calling_funcs():
    foo(1, 2, 'a', 2, 7, "198hd", idk="kwarg1_val", yes="ofcourse")
    # you can unpack tuples and lists as function args
    my_list = list()
    my_tuple = tuple()
    foo(*my_list, *my_tuple)  # the lenght of the itreable you want to
    # unpack must the same as the number of args

    # unpacking keyword args
    my_dict = dict()  # keyword - value, keys must match the kwargs parameters
    foo(*my_tuple, **my_dict)

    foo1()
    print(my_value)

    my_list = [i for i in range(10)]
    foo2(my_list)
    print(my_list)


# MODIFYING GLOBAL VARIABLES aka not inside functions

my_value = 0


def foo1():
    global my_value
    my_value = 1237  # writing only this won't modify the variable and will
    # create a local variable with the name 'my_value'


# MUTABLE OBJECTS WILL BE MODIFIED WITHIN A FUNCTION

def foo2(a_list):
    # reinitializing/rebinding the list
    a_list = [i * i for i in range(4)]
    a_list = a_list + [200, 300, 400]
    #  NOT  reinitializing/rebinding the list aka affects the original list
    a_list += [100, 200, 300]

    a_list.append(1029)  # this will modify the original list unless you
    # rebind the reference


"""
You can specify the type of an argument by using:
my_arg_name: type

To assign a default value:
my_arg_name: type = __my_data_type__

"""


# specify what type the function returns with '->', doesn't impact code
def some_foo(my_list: list, index: int, name: str = "") -> None:
    pass


"""
Use the 'typing' import in order to specify argument types even more clearly
"""

"""
***

With the typing module comes with a pretty comprehensive collection of type hints, including:

List, Tuple, Set, Map - for list, tuple, set and map respectively.
Iterable - useful for generators.
Any - when it could be anything.
Union - when it could be anything within a specified set of types, as opposed to Any.
Optional - when it might be None. Shorthand for Union[T, None].
TypeVar - used with generics.
Callable - used primarily for functions, but could be used for other callables.

***
"""

from typing import List, Tuple


def my_foo(some_list: List[str], t: Tuple[int]):
    pass
