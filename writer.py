import time
import random
import string
from multiprocessing.managers import BaseManager

class SharedQueueManager(BaseManager):
    pass

SharedQueueManager.register('SharedQueue')

def generate_random_message(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def writer():
    manager = SharedQueueManager(address=('localhost', 50000), authkey=b'queue')
    manager.connect()
    shared_queue = manager.SharedQueue()

    while True:
        message = generate_random_message()
        shared_queue.put(message)
        print(f"Produced: {message}")
        time.sleep(2)  # Reduced sleep time for quicker demonstration

if __name__ == '__main__':
    writer()
