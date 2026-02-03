## BST deletion Implementation
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insertNode(self, data):
        if self.value is None:
            self.value = data
            return
        if self.value == data:
            return
        if self.value > data:
            if self.left:
                self.left.insertNode(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.insertNode(data)
            else:
                self.right = BinarySearchTree(data)
    
    def search(self, data):
        if self.value == data:
            print(f"Node {data} found in the tree")
            return
        if data < self.value:
            if self.left:
                self.left.search(data)
            else:
                print(f"Node {data} not found in the tree...")
        else:
            if self.right:
                self.right.search(data)
            else:
                print(f"Node {data} not found in the tree...")
    
    def preorder_traversal(self):
        print(self.value, end= " ")
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()
    
    def deleteNode(self, data, curr):
        if self.value is None:
            print("Tree is empty!")
            return
        if data < self.value:
            if self.left:
                self.left = self.left.deleteNode(data, curr)
            else:
                print(f"\nNode {data} not present in the tree.")
        elif data > self.value:
            if self.right:
                self.right = self.right.deleteNode(data, curr)
            else:
                print(f"\nNode {data} not present in the tree.")
        else:
            if self.left is None:
                temp = self.right
                if data == curr:
                    self.value = temp.value
                    self.left = temp.left
                    self.right = temp.right
                    temp = None
                    return
                self = None
                return temp
            if self.right is None:
                temp = self.left
                if data == curr:
                    self.value = temp.value
                    self.left = temp.left
                    self.right = temp.right
                    temp = None
                    return
                self = None
                return temp
            node = self.right
            while node.left:
                node = node.left
            self.value = node.value
            self.right = self.right.deleteNode(node.value, curr)
        return self
    
    def find_min_node(self):
        current = self
        while current.left:
            current = current.left
        print(f"Minimum node value is: {current.value}")
    
    def find_max_node(self):
        current = self
        while current.right:
            current = current.right
        print(f"Maximum node value is: {current.value}")

def count(node):
        if node is None:
            return 0
        else:
            return 1 + count(node.left) + count(node.right)



root  = BinarySearchTree(10)
list1= [5,15,20,25,30,35]
for i in list1:
    root.insertNode(i)
print(f"node count is : {count(root)}")
print(root.find_min_node())
print(root.find_max_node())
print("\nPreorder Traversal before deletion ====>")
root.preorder_traversal()
if count(root) > 1:
    root.deleteNode(10, 10)
else:
    print("Tree has only one node, deletion not possible.")
# root.deleteNode(100)
# root.deleteNode(20)
print("\ntravesal after deletion ====>")
root.preorder_traversal()