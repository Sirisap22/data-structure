class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data) 
    
    def dequeue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0
    
init, order = input('Enter Input : ').split('/')

init = list(map(int, init.lstrip().split(' ')))

order = order.split(',')

q = Queue()

for ele in init:
    q.enqueue(ele)

for act in order:
    if act[0] == 'E':
        q.enqueue(int(act.split(' ')[1]))
    elif act[0] == 'D':
        q.dequeue()

count = {}
is_duplicate = False

while not q.isEmpty():
    key = q.dequeue()

    if key not in count:
        count[key] = 1
    else:
        is_duplicate = True
        break

if is_duplicate:
    print('Duplicate')
else:
    print('NO Duplicate')
    
