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

class Stack:
    """ class Stack 
        default : empty stack / Stack([...])
    """
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        if self.isEmpty():
          return ''
        s = ''
        for i, ele in enumerate(self.items):
            s += str(ele)
            if i != len(self.items)-1:
              s += ', '
        return s
    def push(self, i):
        self.items.append(i)

    def pop(self):   #edit code
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

real, mirror = input("Enter Input (Normal, Mirror) : ").split(' ')

s = Stack()
h = Stack()
q = Queue()
mirror_remain = ''
real_remain = ''
for c in mirror[::-1]:
  if s.isEmpty():
    while not h.isEmpty() and h.peek() == c:
      s.push(h.pop())
    s.push(c)

  elif s.peek() == c:
    s.push(c)
  
  else:
    while not s.isEmpty():
      h.push(s.pop())
    s.push(c)

  if s.size() == 3:
    q.enQueue(s.peek())
    while not s.isEmpty():
      s.pop()

while not s.isEmpty():
  mirror_remain += s.pop()
while not h.isEmpty():
  mirror_remain += h.pop()

real_explosives = 0
mirror_explosives = q.size()
failed_interrupted = 0
for c in real:
  if s.isEmpty():
    while not h.isEmpty() and h.peek() == c:
      s.push(h.pop())
    s.push(c)

  elif s.peek() == c:
    s.push(c)
  
  else:
    while not s.isEmpty():
      h.push(s.pop())
    s.push(c)

  if s.size() == 3:
    if not q.isEmpty():
      item = q.deQueue()
      if item == s.peek():
        failed_interrupted += 1
        while not s.isEmpty():
          s.pop()
        s.push(item)
      else:
        while s.size() > 1:
          h.push(s.pop())
        h.push(item)
        h.push(s.pop())
    else:
      real_explosives += 1
      while not s.isEmpty():
        s.pop()

while not s.isEmpty():
  real_remain += s.pop()
while not h.isEmpty():
  real_remain += h.pop()

print("NORMAL :")
print(len(real_remain))
print(real_remain if len(real_remain) != 0 else "Empty")
print(f"{real_explosives} Explosive(s) ! ! ! (NORMAL)")
if failed_interrupted > 0:
  print(f"Failed Interrupted {failed_interrupted} Bomb(s)")
print("------------MIRROR------------")
print("MIRROR :"[::-1])
print(len(mirror_remain))
print(mirror_remain if len(mirror_remain) != 0 else "Empty"[::-1])
print(f"{mirror_explosives} Explosive)s( ! ! ! )MIRROR("[::-1])