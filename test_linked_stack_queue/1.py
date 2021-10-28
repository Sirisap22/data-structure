class Stack:
    def __init__(self):
        self.stack = []
    
    def __str__(self):
        s = ''
        s += 'Data in Stack is : '
        for i, ele in enumerate(self.stack):
            if i == self.size()-1:
                s += str(ele)
            else:
                s += f'{ele} '
        
        return s

    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

    def peek(self):
        return self.stack[-1]
    
    def bottom(self):
        return self.stack[0]

ch = input('Enter choice : ')

if ch == '1':
    s1 = Stack()
    s1.push(10)
    s1.push(20)
    print(s1)
    s1.pop()
    s1.push(30)
    print("Peek of stack :",s1.peek())
    print("Bottom of stack :",s1.bottom())

elif ch == '2':
    s1 = Stack()
    s1.push(100)
    s1.push(200)
    s1.push(300)
    s1.pop()
    print(s1)
    print("Stack is Empty :",s1.isEmpty())

elif ch == '3':
    s1 = Stack()
    s1.push(11)
    s1.push(22)
    s1.push(33)
    s1.pop()
    print(s1)
    print("Stack size :",s1.size())
