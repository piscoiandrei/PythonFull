"""
USING 'await'

1. when calling an 'async' function aka an awaitable object
2. you can't call an async function from a synchronous function/module
3. you can't use await outside functions
"""


async def greet(name):
    return "Hi, my name is " + name


def run(coroutine):
    try:
        coroutine.send(None)
    except StopIteration as e:
        return e.value


async def main():
    names = ['Bob', 'Jack', 'Anna', 'Pewds']
    for name in names:
        print(await greet(name))


# run(main())

#
# ANOTHER EXAMPLE
#

async def fibo(n):
    if n < 2:
        return 1
    else:
        return await fibo(n - 1) + await fibo(n - 2)


async def compute():
    for n in range(10):
        print(await fibo(n))


run(compute())
