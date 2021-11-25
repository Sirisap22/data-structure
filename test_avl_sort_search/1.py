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
        self.count_path = 0
    
    def insert(self, data):
        root = self.root

        self.root = self._insert(root, data)
    
    def _insert(self, root, data):
        if root is None:
            return TreeNode(data)
        
        elif data >= root.data:
            root.right = self._insert(root.right, data)
        else:
            root.left = self._insert(root.left, data)
        
        return root
    
    def search(self, target):
        self.count_path = 0
        return self.bfs(target)
    
    def bfs(self, target):
        if self.root is None:
            return 0

        queue = [(self.root, 0)]

        while len(queue) != 0:
            cur_root, cur_sum = queue.pop(0)
            if cur_root is None or cur_sum > target:
                continue
            
            cur_sum += cur_root.data
            if cur_sum == target:
                self.count_path += 1
                
            queue.append((cur_root.left, cur_sum))
            queue.append((cur_root.right, cur_sum))
        
        return self.count_path


arr, target = input("Enter number / sum : ").split("/")
arr = list(map(int, arr.split(" ")))

bst = BST()
for ele in arr:
    root = bst.insert(ele)

ans = bst.search(int(target))
if ans == 0:
    print("ANS: NO PATH")
else:
    print(f"ANS: {ans}")
    