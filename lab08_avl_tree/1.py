class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insertWithPath(self, val):  
        path = ''

        if self.root is None:
            root = Node(val)
            self.root = root
            path += '*'
            return path

        current = self.root
        while True:
            if val > current.data:
                if current.right is None:
                    current.right = Node(val)
                    path += 'R*'
                    break
                else:
                    current = current.right
                    path += 'R'
            elif val < current.data:
                if current.left is None:
                    current.left = Node(val)
                    path += 'L*'
                    break
                else:
                    current = current.left
                    path += 'L'
            else:
                break

        return path
    
arr = list(map(int, input('Enter Input : ').split(' ')))

bst = BinarySearchTree()
for ele in arr:
    path = bst.insertWithPath(ele)
    print(path)
