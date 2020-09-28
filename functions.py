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