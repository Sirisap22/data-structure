class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST():
    def __init__(self):
        self.rank = 0
        self.is_found = False
    
    def insert(self, root, data):
        if root is None:
            return TreeNode(data)

        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        return root

    def find_rank(self, root, data):
        min_val = self.min_value(root)
        if min_val is None:
            return None
        
        min_val = min_val.data

        if data < min_val:
            return 0
        elif data == min_val:
            return 1
        else:
            self.rank = 0
            self.is_found = False
            return self.traverse(root, data)

    def traverse(self, root, data):
        if root is None:
            return float('inf')
        
        if not self.is_found:
            self.traverse(root.left, data)

        if not self.is_found:
        ## do something  
            if data < root.data:
                self.is_found = True
            elif data == root.data:
                self.rank += 1
                self.is_found = True
            else:
                self.rank += 1

        if not self.is_found:
            self.traverse(root.right, data)

    
    def min_value(self, root):
        if root is None or root.left is None:
            return root
        else:
            min_root = self.min_value(root.left)
        
        return min_root

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

arr, rank = input('Enter Input : ').split('/')
arr = list(map(int, arr.split(' ')))
to_rank = int(rank)

root = None
bst = BST()

for ele in arr:
    root = bst.insert(root, ele)

printTree90(root)
print('--------------------------------------------------')
rank = bst.find_rank(root, to_rank)
print(f'Rank of {to_rank} : {bst.rank}')


        


