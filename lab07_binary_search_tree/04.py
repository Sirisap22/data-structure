class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):  
        if self.root is None:
            root = Node(val)
            self.root = root
            return
        current = self.root

        while True:
            if val > current.data:
                if current.right is None:
                    current.right = Node(val)
                    break
                else:
                    current = current.right
            elif val < current.data:
                if current.left is None:
                    current.left = Node(val)
                    break
                else:
                    current = current.left
            else:
                break
        
        return self.root

    def delete(self, r, data):
        if r is None:
            return r
        
        if data < r.data:
            r.left = self.delete(r.left, data)
        elif data > r.data:
            r.right = self.delete(r.right, data)
        else:
            if r.left is None:
                temp = r.right
                r = None
                return temp
            
            elif r.right is None:
                temp = r.left
                r = None
                return temp

            temp = self.min_value_node(r.right)

            r.data = temp.data

            r.right = self.delete(r.right, temp.data)
        
        return r
    
    def can_delete(self, data):
        if self.root is None:
            return False
        current = self.root
        while current is not None:
            if data == current.data:
                return True
            elif data > current.data:
                current = current.right
            else:
                current = current.left 
        
        return False

    def min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current
        

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
data = list(map(lambda x: x.split(' '), data))
for ele in data:
    if ele[0] == 'i':
        tree.insert(int(ele[1]))
        print(f'insert {ele[1]}')
        printTree90(tree.root)
    elif ele[0] == 'd':
        print(f'delete {ele[1]}')
        if tree.can_delete(int(ele[1])):
            tree.root = tree.delete(tree.root, int(ele[1]))
        else:
            print("Error! Not Found DATA")
        printTree90(tree.root)
