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
        self.stc = Stack()
        self.max = 0
    def push(self, val):
        if val in self.count.keys():
            self.count[val] += 1
        else:
            self.count[val] = 1
        self.stc.push(val)
        self.max = max(self.count.values())
    def pop(self):
        i = self.stc.delet()
        res = [i]
        while self.count[i] != self.max:
            i = self.stc.delet()
            res.append(i)
        for k in reversed(res[:-1]):
            self.stc.push(k)
        self.count[i] -= 1
        if self.count[i] < 0:
            self.count[i] = 0
        self.max = max(self.count.values())
        return i



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
