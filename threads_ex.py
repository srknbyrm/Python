from threading import Thread, Lock, current_thread
from queue import Queue
import time

# database_value = 0
#
#
# def increase(lock):
#     global database_value
#     with lock:
#         local_copy = database_value
#     # processing
#         local_copy += 1
#         time.sleep(0.1)
#         database_value = local_copy
#
#
# lock = Lock()
# print('start value', database_value)
#
# thread1 = Thread(target=increase, args=(lock,))
# thread2 = Thread(target=increase, args=(lock,))
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print('end value', database_value)
# print('end main')

q = Queue()
lock = Lock()


# q.put(1)
# q.put(2)
# q.put(3)
#
# first = q.get()
# q.task_done()
# q.join()  # Block the main thread until queue process finish
# print(first)

def worker(q, lock):
    while True:
        value = q.get()
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()



num_threads = 10
for i in range(num_threads):
    thread = Thread(target=worker, args=(q, lock))
    thread.daemon = True  # if we do not use daemon thread program will continue because of while true loop
    thread.start()

for i in range(1, 21):
    q.put(i)

q.join()

print('end main')
