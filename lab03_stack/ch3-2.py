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

arr = [ ele.split(' ') for ele in input("Enter Input : ").split(',')]
s = Stack()
s2 = Stack()
for ele in arr:
  if ele[0] == 'A':
    s.push(int(ele[1]))
    print(f"Add = {ele[1]}")
  else:
    if s.isEmpty():
      print('-1')
      continue

    elif ele[0] == 'P':
      print(f"Pop = {s.pop()}")

    elif ele[0] == 'D':
      while(not s.isEmpty()):
        if s.peek() == int(ele[1]):
          cur = s.pop()
          print(f"Delete = {cur}")
        else:
          s2.push(s.pop())
      while(not s2.isEmpty()):
        s.push(s2.pop())

    elif ele[0] == 'LD':
      while(not s.isEmpty()):
        if s.peek() < int(ele[1]):
          cur = s.pop()
          print(f"Delete = {cur} Because {cur} is less than {ele[1]}")
        else:
          s2.push(s.pop())
      while(not s2.isEmpty()):
        s.push(s2.pop())

    elif ele[0] == 'MD':
      while(not s.isEmpty()):
        if s.peek() > int(ele[1]):
          cur = s.pop()
          print(f"Delete = {cur} Because {cur} is more than {ele[1]}")
        else:
          s2.push(s.pop())
      while(not s2.isEmpty()):
        s.push(s2.pop())

print(f"Value in Stack = [{s}]")