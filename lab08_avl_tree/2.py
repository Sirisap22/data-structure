class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.val)
  
class AVL_Tree(object): 
    def __init__(self):
        self.insertPath = ''
    
    def insert(self, root, data):
        self.insertPath = ''
        return self._insert(root, data)


    def _insert(self, root, data):
        # Feed forward
        if root is None:
            return TreeNode(data)
        elif data < root.val:
            self.insertPath += 'L'
            root.left = self._insert(root.left, data)
        else:
            self.insertPath += 'R'
            root.right = self._insert(root.right, data)
        
        # Update the height
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Back propagation
        balance = self.getBalance(root)

        path = self.insertPath[ -root.height+1: -root.height+3 if -root.height+3 != 0 else None ]

        if balance < -1 or balance > 1:
            print('Not Balance, Rebalance!')
        
        if balance > 1 and  path == 'LL':
            return self.rightRotate(root)
        
        if balance < -1 and path == 'RR':
            return self.leftRotate(root)

        if balance > 1 and path == 'LR':
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        if balance < -1 and path == 'RL':
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def leftRotate(self, x):
        # Remember pin
        y = x.right
        pin = y.left
 
        # Perform rotation
        y.left = x
        x.right = pin
 
        # Update heights
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
 
        # Return the new root
        return y

    def rightRotate(self, x):
        # Remember pin
        y = x.left
        pin = y.right
 
        # Perform rotation
        y.right = x
        x.left = pin
 
        # Update heights
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
 
        # Return the new root
        return y


def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
  
myTree = AVL_Tree() 
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = myTree.insert(root, int(e))
    printTree90(root)
    print("===============")