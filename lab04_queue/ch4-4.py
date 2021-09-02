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


event = ["Eat", "Game", "Learn", "Movie"]
place = ["Res.", "ClassR.", "SuperM.", "Home"]

arr = [ [ele_inner.split(':') for ele_inner in ele.split(' ')] for ele in input("Enter Input : ").split(',')]
my_q = Queue()
crush_q = Queue()

score = 0
my_al = Queue()
crush_al = Queue()
for action in arr:
  my_q.enQueue(action[0])
  crush_q.enQueue(action[1])
  if action[0][0] == action[1][0] and action[0][1] == action[1][1]:
    score += 4
  elif action[0][1] == action[1][1]:
    score += 2
  elif action[0][0] == action[1][0]:
    score += 1
  else:
    score -= 5

print("My   Queue = ", end="")
while not my_q.isEmpty():
  cur = my_q.deQueue()
  print(f"{cur[0]}:{cur[1]}", end="")
  if my_q.size() > 0:
    print(", ", end="")
  my_al.enQueue(f"{event[int(cur[0])]}:{place[int(cur[1])]}")
print()

print("Your Queue = ", end="")
while not crush_q.isEmpty():
  cur = crush_q.deQueue()
  print(f"{cur[0]}:{cur[1]}", end="")
  if crush_q.size() > 0:
    print(", ", end="")
  crush_al.enQueue(f"{event[int(cur[0])]}:{place[int(cur[1])]}")
print()

print("My   Activity:Location = ", end="")
while not my_al.isEmpty():
  print(my_al.deQueue(), end="")
  if my_al.size() > 0:
    print(", ", end="")
print()

print("Your Activity:Location = ", end="")
while not crush_al.isEmpty():
  print(crush_al.deQueue(), end="")
  if crush_al.size() > 0:
    print(", ", end="")
print()

if score >= 7:
  print("Yes! You're my love! : ", end="")
elif score < 7 and score > 0:
  print("Umm.. It's complicated relationship! : ", end="")
else:
  print("No! We're just friends. : ", end="")
print(f"Score is {score}.")




