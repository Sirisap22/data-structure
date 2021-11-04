from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            
        else:
            
            if root.left is None:
                temp = root.right
                root = None
                return temp
            
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            inorder = self.minVal(root.right)
            
            root.val = inorder.val
            
            root.right = self.deleteNode(root.right, inorder.val)
            
        return root
                
    
    
    def minVal(self, root):
        if root is None:
            return root
        
        cur = root
        while cur.left is not None:
            cur = cur.left
        
        return cur