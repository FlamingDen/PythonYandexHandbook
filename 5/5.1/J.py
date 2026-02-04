class Stack:
    def __init__(self):
        self.data = list()

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def is_empty(self):
        return len(self.data) == 0
    
stack = Stack()
for item in range(10):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop(), end=" ")