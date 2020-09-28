from multiprocessing import Process, Value, Array, Lock
from multiprocessing import Queue
from multiprocessing import Pool
import os
import time


# ALWAYS USE THIS IN THE MAIN PROGRAM IN THE
# if __name__ == '__main__':
#    // put stuff here


def processes_no_shared_values():
    def my_func(*args):
        for i in range(100):
            x = i * i
            time.sleep(0.1)

    processes = []
    num_processes = os.cpu_count()

    # create processes
    for k in range(num_processes):
        p = Process(target=my_func, args=(1, 3, "arggggs"))  # args = tuple()
        processes.append(p)

    # start
    for p in processes:
        p.start()

    # join,waiting for processes to finish, while waiting
    # the main thread is locked
    for p in processes:
        p.join()

    print('end main')


# SHARED VALUES

def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1


def processes_shared_value():
    lock = Lock()
    shared_number = Value('i', 0)  # i from int
    print("number at beginning is ", shared_number.value)
    p1 = Process(target=add_100, args=(shared_number, lock))
    p2 = Process(target=add_100, args=(shared_number, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("number at end is ", shared_number.value)


def add_800(numbers, lock):
    for i in range(800):
        time.sleep(0.001)
        for j in range(len(numbers)):
            with lock:
                numbers[j] += 1


def processes_shared_array():
    lock = Lock()
    shared_array = Array('d', [0.0, 1.1, 1013.193])  # d from double
    print("arrray is beginning is ", shared_array[:])

    p1 = Process(target=add_800, args=(shared_array, lock))
    p2 = Process(target=add_800, args=(shared_array, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("array at end is ", shared_array[:])


# EXCHANGING DATA BETWEEN MULTIPLE PROCESSES

def square(numbers, queue):
    for i in numbers:
        queue.put(i * i)


def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1 * i)


def data_exchange_queue():
    numbers = range(1, 6)
    q = Queue()

    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())  # remove and return first element


# Process Pool

def cube(number):
    return number ** 3


def process_pool():
    # most important methods:
    # map, apply, join, close   # map is not the basic python map function
    pool = Pool()

    numbers = range(10)
    result = pool.map(cube, numbers)  # splits the iterable to multiple
    # equally sized chunks to be computed in parallel by multpile processes
    # usually the number of cpu cores/threads in your pc
    pool.close()
    pool.join()

    print(result)
