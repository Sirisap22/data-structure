class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.val)


class AVL_Tree(object):

    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key < root.right.val:
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
        y = x.right
        pin = y.left

        y.left = x
        x.right = pin

        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, x):
        y = x.left
        pin = y.right

        y.right = x
        x.left = pin

        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

tree = AVL_Tree()
root = None

arr = input("Input: ").split(" ")
for ele in arr:
    root = tree.insert(root, int(ele))
printTree90(root)
