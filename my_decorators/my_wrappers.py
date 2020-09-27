import time
import functools


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()

        ret_val = func(*args, **kwargs)

        total = time.time() - start
        print("Execution time: ", total)
        return ret_val

    return wrapper


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")

        result = func(*args, **kwargs)

        print(f"{func.__name__} returned {result}")
        return result

    return wrapper
