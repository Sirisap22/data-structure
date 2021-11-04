arr = list(map(int, input().split(' '))).sort()

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
# [ int(ele) for ele in input().split(' ') ]

def b_tree(lis):
    mid = len(lis) //2

    root = TreeNode(lis[mid])
    root.right = b_tree(lis[mid+1:])
    root.left = b_tree(lis[:mid])

    return root

