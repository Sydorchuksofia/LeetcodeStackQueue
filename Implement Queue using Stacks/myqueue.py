class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    def push(self, value):
        new = Node(value)
        new.next = self.top
        self.top = new
    def pop(self):
        if not self.top:
            return None
        v = self.top.value
        self.top = self.top.next
        return v
    def peek(self):
        if self.top:
            return self.top.value
        return None
    def is_empty(self):
        if self.top:
            return False
        return True

class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack() 
    def push(self, x: int):
        self.stack1.push(x)
    def pop(self) -> int:
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
    def peek(self) -> int:
        if self.stack2.is_empty():
              while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()
    def empty(self) -> bool:
        return self.stack1.is_empty() and self.stack2.is_empty()
