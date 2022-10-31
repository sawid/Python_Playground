class Stack():

        def __init__(self):
                self.items = []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            return self.items.pop()

        def peek(self):
                return self.items[-1]

        def isEmpty(self):
            if len(self.items == 0):
                return True
            return  False

        def size(self):
            return len(self.items)

stack = Stack()

stack.push("A")
stack.push("B")

for i in stack.items:
        print(stack.peek())