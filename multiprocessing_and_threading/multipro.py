from multiprocessing import Process
import os
import time
# TAKES A LONG TIME TO START

def my_func(*args):
    for i in range(100):
        x = i * i
        time.sleep(0.1)


processes = []
num_processes = os.cpu_count()

# create processes
for k in range(num_processes):
    p = Process(target=my_func(), args=(1, 3, "arggggs"))
    processes.append(p)

# start
for p in processes:
    p.start()

# join,waiting for processes to finish, while waiting the main thread is locked
for p in processes:
    p.join()

print('end main')
