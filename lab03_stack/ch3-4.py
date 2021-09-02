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
class StackCalc():
    def __init__(self):
      self.s = Stack()
    
    def run(self, arg):
      arr = arg.split(' ')
      for ele in arr:
          if ele.lstrip('-').isdigit():
            self.s.push(int(ele))
          elif ele == "DUP":
            ele1 = self.s.pop()
            self.s.push(ele1)
            self.s.push(ele1)
          elif ele == "POP":
            self.s.pop()
          elif ele == '+' or ele == '*' or ele == '/' or ele == '-': 
            ele1 = self.s.pop();
            ele2 = self.s.pop();
            result = 0;
            if ele == '+':
              result = ele1 + ele2
            elif ele == '*':
              result = ele1 * ele2
            elif ele == '/':
              result = ele1 / ele2
            elif ele == '-':
              result = ele1 - ele2
            self.s.push(result)
          else: 
            print(f"Invalid instruction: {ele}")
            exit(0)
    def getValue(self):
      if self.s.isEmpty():
        return 0
      return int(self.s.pop())



print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())