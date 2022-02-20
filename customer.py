from abc import ABC, abstractmethod
from reg import Register
from functools import reduce

'''this class defines the two different classes of customers'''

class Customer(ABC):
    def __init__(self, type='A'):
        self.type = type
        self.items = 0

        self.register_assigned = None

    @abstractmethod
    def choose_register(self):
        pass

class CustomerA(Customer):
    def __init__(self, time, items):
        self.items = items
        self.time = time
    def choose_register(self, register_list):
        self.register_assigned = reduce(lambda x,y:x if x.queue.size<=y.queue.size else y,register_list)
        self.register_assigned.queue.enqueue(self)

class CustomerB(Customer):
    def __init__(self, time, items):
        self.items = items
        self.time = time
        self.register_assigned_to = 0
    def choose_register(self, register_list):
        for r in register_list:
            if r.queue.isEmpty():
                self.register_assigned = r
                self.register_assigned.queue.enqueue(self)
                return
        self.register_assigned = reduce(lambda x,y:x if x.queue.queue[x.queue.rear-1].items <= y.queue.queue[y.queue.rear-1].items else y, register_list)
        self.register_assigned.queue.enqueue(self)

