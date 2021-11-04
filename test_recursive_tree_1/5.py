class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self) :
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root ,data)
        return self.root
        
    def _insert(self, root, data):
        if root is None:
            return Node(data)
        
        elif data < root.data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)

        return root
    
    def min_val(self):
        cur = self.root
        if cur is None:
            return None
        
        while cur.left is not None:
            cur = cur.left
        
        return cur.data

    def max_val(self):
        cur = self.root
        if cur is None:
            return None
        
        while cur.right is not None:
            cur = cur.right
        
        return cur.data

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print('-' * 50)
print(f'Min : {T.min_val()}')
print(f'Max : {T.max_val()}')