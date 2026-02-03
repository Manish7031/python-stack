## BST Traversal Implementations - pre order, in-order, post-order

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
    
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value, end= " ")
        if self.right:
            self.right.inorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value, end= " ")
    

root  = BinarySearchTree(10)
list1= [20,30, 5, 15, 25, 35]
for i in list1:
    root.insertNode(i)
print("Pre-order Traversal of BST:")
root.preorder_traversal()
print("\nIn-order Traversal of BST:")
root.inorder_traversal()
print("\nPost-order Traversal of BST:")
root.postorder_traversal()