class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            root = Node(data)
            self.root = root
            return
        current = self.root

        while True:
            if data >= current.data:
                if current.right is None:
                    current.right = Node(data)
                    break
                else:
                    current = current.right
            else:
                if current.left is None:
                    current.left = Node(data)
                    break
                else:
                    current = current.left
        
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def min_value(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.data
    
    def max_value(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
print(f'Min : {T.min_value()}')
print(f'Max : {T.max_value()}')