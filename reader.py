import time
from multiprocessing.managers import BaseManager

class SharedQueueManager(BaseManager):
    pass

SharedQueueManager.register('SharedQueue')

def reader():
    manager = SharedQueueManager(address=('localhost', 50000), authkey=b'queue')
    manager.connect()
    shared_queue = manager.SharedQueue()

    while True:
        if not shared_queue.empty():
            message = shared_queue.get()
            if message:
                print(f"Consumed: {message}")
        else:
            print("No message in the queue")
        time.sleep(2)

if __name__ == '__main__':
    reader()
