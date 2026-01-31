## single linkedlist

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
    
    def add_nodeAtBegin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    def add_nodeAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            sh = self.head
            while sh.ref is not None:
                sh = sh.ref
            sh.ref = new_node

    def deleteNode_begin(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            print("Node deleted from the beginning : ", self.head.data)
            self.head = self.head.ref
    
    def deleteNode_End(self):
        if self.head is None:
            print("Linked List is empty")
        if self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
                print("Node deleted from the end : ", n.ref.data)
            n.ref = None
            

    def delete_by_value(self, x):
        if self.head is None:
            print("Linked List is empty")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present in linked list")
        else:
            n.ref = n.ref.ref



ll1 = LinkedList()
# ll1.add_nodeAtBegin(10)
# ll1.add_nodeAtBegin(20)
# ll1.add_nodeAtBegin(30)
# ll1.add_nodeAtEnd(40)
# ll1.add_nodeAtEnd(50)
ll1.add_nodeAtBegin(10)
ll1.add_nodeAtBegin(20)
ll1.add_nodeAtBegin(30)
ll1.add_nodeAtEnd(40)
# ll1.deleteNode_begin()
# ll1.deleteNode_End()
ll1.delete_by_value(20)
ll1.delete_by_value(100) 
ll1.print_LL()