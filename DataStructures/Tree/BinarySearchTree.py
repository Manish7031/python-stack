## BST implemntation

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

root  = BinarySearchTree(10)
# print(f"Root node value => {root.value}")
# print(f"Left node value => {root.left}")
list1 = [20, 4, 25, 100, 1, 15, 6]
for i in list1:
    root.insertNode(i)

search_values = [25, 15, 99, 150]
for val in search_values:
    root.search(val)
    
