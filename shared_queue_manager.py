import multiprocessing
from multiprocessing.managers import BaseManager

class SharedQueueManager(BaseManager):
    pass

class SharedQueue:
    def __init__(self):
        self.manager = multiprocessing.Manager()
        self.queue = self.manager.list()
        self.lock = multiprocessing.Lock()

    def put(self, item):
        with self.lock:
            self.queue.append(item)

    def get(self):
        with self.lock:
            if len(self.queue) > 0:
                return self.queue.pop(0)
            return None

    def empty(self):
        with self.lock:
            return len(self.queue) == 0

shared_queue = SharedQueue()

def get_queue():
    return shared_queue

SharedQueueManager.register('SharedQueue', callable=get_queue)

if __name__ == '__main__':
    manager = SharedQueueManager(address=('', 50000), authkey=b'queue')
    server = manager.get_server()
    print("Server started at port 50000")
    server.serve_forever()
