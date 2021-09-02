from collections import deque
class Queue:
    def __init__(self, q = None):
      if q == None:
        self.items = deque()
      else:
        self.items = deque(q,len(q))
    def __str__(self):
        if (self.isEmpty()):
          return ""
        s = ''
        for i, ele in enumerate(self.items):
          if i != self.size()-1:
            s += repr(str(ele))+', '
          else:
            s += repr(str(ele))
        return s
    def enQueue(self, i):
      self.items.append(i)

    def deQueue(self):
      return self.items.popleft()

    def isEmpty(self):
      return len(self.items) == 0

    def size(self):
      return len(self.items)

q_main = Queue([char for char in input("Enter people : ")])
q_1 = Queue()
q_2 = Queue()
minutes = 1
while not q_main.isEmpty():
  print(minutes, end="")
  if minutes != 1:
    if not q_1.isEmpty() and (minutes-1)%3 == 0:
      q_1.deQueue()
    if not q_2.isEmpty() and (minutes)%2 == 0:
      q_2.deQueue()

  customer = q_main.deQueue()
  if q_1.size() < 5:
    q_1.enQueue(customer)
  elif q_2.size() < 5:
    q_2.enQueue(customer)
  minutes += 1
  print(f" [{q_main}] [{q_1}] [{q_2}]")