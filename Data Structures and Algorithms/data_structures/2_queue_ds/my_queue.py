from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def peak(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)


def queue_challenge():
    q = Queue()
    word_list = ["wore", "a", "silly", "hat", "the", "aadvark"]
    for word in word_list[4:]:
        q.enqueue(word)
    for word in word_list[0:4]:
        q.enqueue(word)
    return q.items
