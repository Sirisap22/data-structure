from collections import deque
class Queue:
    def __init__(self, q = None):
      if q == None:
        self.items = deque()
      else:
        self.items = deque(q,len(q))
    def __str__(self):
        if (self.isEmpty()):
          return "Empty"
        s = ''
        for ele in self.items:
          s += str(ele)+' '
        return s
    def enQueue(self, i):
      self.items.append(i)

    def deQueue(self):
      return self.items.popleft()

    def isEmpty(self):
      return len(self.items) == 0

    def size(self):
      return len(self.items)

arr = [ele.split(' ') for ele in input("Enter Input : ").split(',')]
q = Queue()
for event in arr:
  if event[0] == 'E':
    q.enQueue(event[1])
    print(q.size())
  elif event[0] == 'D':
    if q.isEmpty():
      print(-1)
      continue
    print(f"{q.deQueue()} 0")
print(q)
