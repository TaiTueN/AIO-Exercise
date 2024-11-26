class Queue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Underflow!')
        return self.__queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            raise IndexError('Overflow!')
        self.__queue.append(value)

    def front(self):
        if self.is_empty():
            raise IndexError('Underflow!')
        return self.__queue[0]


queue1 = Queue(capacity=5)

queue1.enqueue(1)
queue1.enqueue(2)

print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())
print(queue1.front())
print(queue1.dequeue())
print(queue1.is_empty())
