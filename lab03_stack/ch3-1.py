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
          return 'Empty'
        s = ''
        for ele in self.items:
            s += str(ele)+' '
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
for ele in arr:
  cur = None
  if ele[0] == 'A':
    cur = ele[1]
    s.push(ele[1])
    print(f"Add = {cur} and Size = {s.size()}")
  else:
    if s.isEmpty():
      print('-1')
      continue
    cur = s.pop()
    print(f"Pop = {cur} and Index = {s.size()}")
print(f"Value in Stack = {s}")