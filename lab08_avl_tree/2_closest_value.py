class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        self.closes_val = {
            "delta": float('inf'),
            "node": None
        }
        
    
    def insert(self, data):
        root = self.root
        self.root = self._insert(root, data)
        return self.root
    
    def _insert(self, root, data):
        if root is None:
            return TreeNode(data)
        elif root.data >= data:
            root.right = self._insert(root.right, data)
        else:
            root.left = self._insert(root.left, data)
        return root
    
    def traverse(self, root, target):
        if root is None:
            return root
        
        self.traverse(root.left, target)

        delta = abs(target - root.data)
        if delta < self.closest_val["delta"]:
            self.closest_val["delta"] = delta
            self.closest_val["node"] = root.data
            
        self.traverse(root.right, target)

    
    def closest_value(self, target):
        self.closest_val = {
            "delta": float('inf'),
            "node": None
        }

        self.traverse(self.root, target)

        return self.closest_val["node"]
        
        

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.left, level + 1)
        print('     ' * level, node)
        printTree90(node.right, level + 1)
        
arr, target = input("Enter Input : ").split("/")
arr = list(map(int, arr.split(" ")))

bst = BST()
for ele in arr:
    root = bst.insert(ele) 
    printTree90(root)
    print("--------------------------------------------------")
print(f"Closest value of {target} : {bst.closest_value(int(target))}")

        
            

