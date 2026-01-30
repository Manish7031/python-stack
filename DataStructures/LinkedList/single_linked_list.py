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
# Example usage:

ll1 = LinkedList()
ll1.add_nodeAtBegin(10)
ll1.add_nodeAtBegin(20)
ll1.add_nodeAtBegin(30)
ll1.add_nodeAtEnd(40)
ll1.add_nodeAtEnd(50)
ll1.print_LL()