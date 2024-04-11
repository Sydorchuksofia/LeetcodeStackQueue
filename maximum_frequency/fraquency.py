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
    def delet(self):
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

class FreqStack:
    def __init__(self):
        self.count = {}
        self.stc = {}
        self.max = 0
    def push(self, val):
        if val in self.count.keys():
            self.count[val] += 1
        else:
            self.count[val] = 1
        if self.count[val] in self.stc:
            self.stc[self.count[val]].push(val)
        else:
            self.stc[self.count[val]] = Stack()
            self.stc[self.count[val]].push(val)
        self.max = max(self.stc.keys())

    def pop(self):
        el = self.stc[self.max].delet()
        self.count[el] -= 1
        if self.stc[self.max].is_empty():
            del self.stc[self.max]
        if not self.stc.get(self.max):
            self.max -= 1
        return el

