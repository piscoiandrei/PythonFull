import asyncio
import datetime


def print_time():
    print(datetime.datetime.now())


async def keep_printing(name: str = "") -> None:
    while True:
        print(name, end=" ")
        print_time()
        await asyncio.sleep(0.5)


asyncio.run(asyncio.wait_for(keep_printing(), 10))
