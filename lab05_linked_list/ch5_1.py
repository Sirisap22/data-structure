class SinglyLinkedList :
    class Node :
        def __init__(self, data, next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
        
    def __init__(self):                
            self.head = None
            self.size = 0
            
    def __str__(self):                
        s = ''
        p = self.head
        while p != None :
            s += str(p.data)
            if p.next != None:
                s += ' <- '
            p = p.next
        return s
          
    def __len__(self) :               
        return self.size         
            
    def isEmpty(self) :               
        return self.size == 0
        
    def indexOf(self,data) :          
        p = self.head
        for i in range(len(self)) :
            if p.data == data :
                return i
            p = p.next
        return -1
            
    def isIn(self,data) :             
        return self.indexOf(data) >= 0
    
    def nodeAt(self,i) :              
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p
    
    def append(self,data):            
        if self.head == None :
          self.head = self.Node(data,None)
          self.size += 1
        else :
          self.insertAfter(len(self)-1,data)   
    
    def insertAfter(self,i,data) :      
        q = self.nodeAt(i)
        p = self.Node(data)
        p.next = q.next
        q.next = p
        self.size += 1
    
    def deleteAfter(self,i) :         
        if self.size > 0 :
          q = self.nodeAt(i)
          q.next = q.next.next
          self.size -= 1
    
    def delete(self,i) :                 
        if i == 0 and self.size > 0 :    
          self.head = self.head.next
          self.size -= 1
        else :
          self.deleteAfter(i-1)          
        
    def removeData(self,data) :         
        if self.isIn(data) :
            self.deleteAfter(self.indexOf(data)-1)

print(" *** Locomotive ***")
arr = [int(x) for x in input("Enter Input : ").split(' ')]
link = SinglyLinkedList()
for ele in arr:
    link.append(ele)

print(f"Before : {link}")

new_head_idx = link.indexOf(0)
new_head = link.nodeAt(new_head_idx)
if  new_head_idx != 0:
    old_tail = link.nodeAt(len(link)-1)
    new_tail = link.nodeAt(link.indexOf(0)-1)

    old_tail.next = link.nodeAt(0)
    new_tail.next = None

    link.head = new_head

print(f"After : {link}")
