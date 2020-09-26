import functools


# FUNCTION DECORATORS

# a decorator is a function that takes another function as argument and
# extends the behaviour of this function without modifying it

def start_end_decorator(func):
    # u need the same args as the function you're wrapping
    # or use this syntax which allows you to put as many args and
    # keyword args as you want

    # prevents losing of identity of func, if you don't add
    # @functtools.wraps(func), func's identity will be changed to wrapper
    # aka func.__name__ will be wrapper
    @functools.wraps(func)  # important
    def wrapper(*args, **kwargs):
        # do something before
        print("Start")

        result = func(*args, **kwargs)

        # do something after
        print("ENd")

        # you also need to return what the function you want to wrap returns
        return result

    return wrapper


@start_end_decorator
def compute(string):  # in the wrapper u need the same args as here
    ns = str(string)[::-1]
    ns = ns.upper()
    print("function executes")
    return ns
