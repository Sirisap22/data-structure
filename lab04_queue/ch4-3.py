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
r = input("Enter code,hint : ")
code = Queue(r[1:-2])
hint = r[-1]
diff = ord(r[0]) - ord(hint)
ans = Queue()
ans.enQueue(hint)
print(f"[{ans}]")
while not code.isEmpty():
  ans.enQueue(chr(ord(code.deQueue()) - diff))
  print(f"[{ans}]")

