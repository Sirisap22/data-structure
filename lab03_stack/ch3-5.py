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

cur_mem = Stack()
helper = Stack()
for event in arr:

  if event[0] == 'A':
    cur_mem.push(int(event[1]))

  elif event[0] == 'S':
    while not cur_mem.isEmpty():
      e = cur_mem.pop()
      if (e%2 == 0):
        e -= 1
        if e < 1:
          e = 1
      else:
        e += 2
      helper.push(e)
    while not helper.isEmpty():
      cur_mem.push(helper.pop())

  elif event[0] == 'B':
    if cur_mem.isEmpty():
      print(0)
      continue

    cur_height = 0
    count = 1
    pre_height = cur_mem.pop()
    helper.push(pre_height)
    while not cur_mem.isEmpty():
      cur_height = cur_mem.pop()
      helper.push(cur_height)
      if cur_height - pre_height > 0:
        pre_height = cur_height
        count += 1
    while not helper.isEmpty():
      cur_mem.push(helper.pop())
    print(count)

    

