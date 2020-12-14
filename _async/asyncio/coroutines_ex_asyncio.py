# SYNC 
import time
import asyncio


def count():
    # 2 seconds
    time.sleep(0.5)
    print(1)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(3)
    time.sleep(0.5)
    print(4)


def main():
    for i in range(3):
        count()

# ASYNC EQUIVALENT


async def count_async():
    # this would take 2s per call in a sync way
    await asyncio.sleep(0.5)
    print('1_async')
    await asyncio.sleep(0.5)
    print('2_async')
    await asyncio.sleep(0.5)
    print('3_async')
    await asyncio.sleep(0.5)
    print('4_async')


async def main_async():
    await asyncio.gather(count_async(), count_async(), count_async())


if __name__ == '__main__':
    t0 = time.perf_counter()
    main()
    t1 = time.perf_counter() - t0
    print(f'Total time elapsed: {t1:0.2f} seconds # SYNC')

    t0 = time.perf_counter()
    asyncio.run(main_async())
    t1 = time.perf_counter() - t0
    print(f'Total time elapsed: {t1:0.2f} seconds # ASYNC')

