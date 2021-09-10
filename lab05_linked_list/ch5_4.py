class VimedList :
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next
    
    def __init__(self, head):
        self.head = self.Node(head)
        self.size = 1
    
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.data) + " "
        while cur.next != None:
            s += str(cur.next.data) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.size == 0
    
    def indexOf(self, data):
        if self.isEmpty():
            return -1

        p = self.head 
        idx = 0
        while p is not None:
            if p.data == data:
                return idx
            p = p.next
            idx += 1

        return -1

    def nodeAt(self, idx):
        if idx > self.size - 1:
            idx = self.size - 1
        elif idx < 0:
            idx = 0

        i = 0
        p = self.head
        while i < idx:
            p = p.next
            i += 1 
        
        return p
    
    def addHead(self, data):
        if self.isEmpty():
            self.head = self.Node(data)
        else:
            old_head = self.head
            self.head = self.Node(data)
            self.head.next = old_head
        self.size +=1
    
    def append(self, data):
        if self.isEmpty():
            self.head = self.Node(data)
        else:
            p = self.head
            while p.next is not None:
                p = p.next
            p.next = self.Node(data)
        self.size +=1
    
    def insertBefore(self, idx, data):
        if idx <= 0:
            self.addHead(data)
        else:
            p = self.nodeAt(idx-1)
            n = p.next

            p.next = self.Node(data, n)
            self.size +=1

    def insertAfter(self, idx, data):
        if idx >= self.size - 1:
            self.append(data)
        else:
            p = self.nodeAt(idx)
            n = p.next

            p.next = self.Node(data, n)
            self.size +=1

    def deleteBefore(self, idx):
        if self.size == 1 or idx == 0:
            return
        
        if idx == 1:
            p = self.nodeAt(idx)
            self.head = p
        else:
            p = self.nodeAt(idx-2)
            n = self.nodeAt(idx)
            p.next = n
        self.size -= 1

    def deleteAfter(self, idx):
        if self.size == 1 or idx == self.size - 1:
            return
        
        p = self.nodeAt(idx)
        n = self.nodeAt(idx+1)
        p.next = n.next

        self.size -= 1
    
    
cmds = [arr.split(' ')for arr in input("Enter Input : ").split(',')]
link = VimedList('|')
for cmd in cmds:
    cursor = link.indexOf('|')
    if cmd[0] == 'I':
        link.insertBefore(cursor, cmd[1])
    elif cmd[0] == 'L':
        link.insertBefore(cursor-1, '|')
        link.deleteAfter(cursor)
    elif cmd[0] == 'R':
        link.insertAfter(cursor+1, '|')
        link.deleteBefore(cursor+1)
    elif cmd[0] == 'B':
        link.deleteBefore(cursor)
    else:
        link.deleteAfter(cursor)
print(link)