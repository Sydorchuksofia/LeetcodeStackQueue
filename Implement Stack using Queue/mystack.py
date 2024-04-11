class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def is_empty(self):
        return self.head is None
    def push(self, item):
        if self.head is None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next
    def pop(self):
        if self.head:
            item = self.head
            self.head = self.head.next
            return item.value
        raise ValueError()
    @property
    def peek(self):
        return self.head.value
    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
class MyStack:
    def __init__(self):
        self.one = Queue()
        self.two = Queue()
    def push(self, x: int) -> None:
        self.one.push(x)
    def pop(self) -> int:
        while len(self.one) > 1:
            self.two.push(self.one.pop())
        p = self.one.pop()
        self.one, self.two = self.two, self.one
        return p
    def top(self) -> int:
        while len(self.one) > 1:
            v = self.one.pop()
            self.two.push(v)
        p = self.one.peek
        self.two.push(self.one.pop())
        self.one, self.two = self.two, self.one
        return p
    def empty(self) -> bool:
        return self.one.is_empty()