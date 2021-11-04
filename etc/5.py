class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST():
    def __init__(self):
        self.s = ''

    def insert(self, root, data):
        if root is None:
            return TreeNode(data)
        
        elif root.data > data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        
        return root
    
    def preorder(self, root):
        self.s = ''
        self._preorder(root)

        return self.s
    
    def _preorder(self, root):
        if root is None:
            return
        
        self.s += f'{root.data} '
        self._preorder(root.left)
        self._preorder(root.right)

    def inorder(self, root):
        self.s = ''
        self._inorder(root)

        return self.s

    def _inorder(self, root):
        if root is None:
            return
        
        self._inorder(root.left)
        self.s += f'{root.data} '
        self._inorder(root.right)

    def postorder(self ):
        pass

    def level(self, root):
        self.s = ''
        q = [root]
        while len(q) != 0:
            sq = [ str(i) for i in q]
            print('queue ', sq)
            cur = q.pop(0)
          
            if cur is not None:
                self.s+= f'{cur.data} '
                q.append(cur.left)
                q.append(cur.right)
        
        return self.s





def printTree(root, depth):
    if root is None:
        return
    printTree(root.right, depth+1)
    print('     '*depth,str(root.data))
    printTree(root.left, depth+1)

arr = list(map(int, input().split(' ')))

bst = BST()

root = None
for ele in arr:
    root = bst.insert(root, ele)

printTree(root, 0)

print(bst.preorder(root))
print(bst.inorder(root))
print(bst.level(root))
