class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def list_to_bst(list_nums):
    middle_idx = int(len(list_nums) / 2)

    if len(list_nums) <= middle_idx:
        return None

    node = TreeNode(list_nums[middle_idx])
    node.left = list_to_bst(list_nums[:middle_idx])
    node.right = list_to_bst(list_nums[middle_idx + 1:])

    return node

def preOrder(node): 
    if not node: 
        return      

    print(node.val)
    preOrder(node.left) 
    preOrder(node.right)   

def printBST(node,level = 0):
    if node != None:
        printBST(node.right, level + 1)
        print('     ' * level, node.val)
        printBST(node.left, level + 1)


list_nums = sorted([int(item) for item in input("Enter list : ").split()])
result = list_to_bst(list_nums)

print("\nList to a height balanced BST : ")
print(preOrder(result))
print("\nBST model : ")
printBST(result)