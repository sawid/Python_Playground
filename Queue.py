from queue import Queue

q = Queue(maxsize=3)

q.put('a')
q.put('b')
q.put('c')

print(q.qsize())

print(q.get())
print(q.get())
print(q.get())

print(q.qsize())

nor,mir = input("Enter Input (Normal, Mirror) : ").split()

print(nor, mir)