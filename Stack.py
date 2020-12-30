class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        # return len(self.items)
        return not self.items
    def peak(self):
        return self.items[-1]
    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    stack = Stack()
    print(stack)
    print(stack.is_empty())
    stack.push(1)
    print(stack)
    stack.push(2)
    stack.push(3)
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.peak())