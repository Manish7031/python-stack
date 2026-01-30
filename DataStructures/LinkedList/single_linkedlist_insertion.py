class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            sh = self.head
            while sh is not None:
                print(sh.data, "->", end=" ")
                sh = sh.ref
        
    def add_nodeAfter(self, data, x):
        n=  self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in linked list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def add_nodeBefore(self, data, x):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present in linked list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty")

    
    def add_nodeAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            sh = self.head
            while sh.ref is not None:
                sh = sh.ref
            sh.ref = new_node


ll1 = LinkedList()
# ll1.add_nodeAtEnd(10)
# ll1.add_nodeAtEnd(20)
# ll1.add_nodeBefore(5,10)
# ll1.add_nodeAfter(30, 10)
ll1.insert_empty(100)
ll1.insert_empty(200)
ll1.print_LL()