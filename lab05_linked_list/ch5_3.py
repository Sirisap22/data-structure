class Node:
    def __init__(self,data,next = None ):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

def createList(l=[]):
    if len(l) == 0:
        return None

    p = Node(int(l[0]))
    head = p
    for data in l[1:]:
        p.next = Node(int(data))
        p = p.next

    return head

def printList(H):
    p = H
    while p is not None:
        print(f"{p} ", end='')
        p = p.next
    print()

def mergeOrderesList(p,q):
    if p.data < q.data:
        m = p
        head = m
        p = p.next
    else:
        m = q
        head = m
        q = q.next

    while p is not None and q is not None:
        if p.data < q.data:
            m.next = p
            p = p.next
        else:
            m.next = q
            q = q.next
        m = m.next

    while p is not None:
        m.next = p
        p = p.next
        m = m.next
    while q is not None:
        m.next = q
        q = q.next
        m = m.next
    
    return head

L1, L2 = [ arr.split(",") for arr in input("Enter 2 Lists : ").split(" ")]
# input only a number save in L1,L2
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)