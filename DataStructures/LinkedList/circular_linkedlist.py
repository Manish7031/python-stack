class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Circular Doubly Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "->", end=" ")
                n = n.nref
                if n == self.head:
                    break
    
    def addNode_AtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.nref = new_node
            new_node.pref = new_node
        else:
            tail = self.head.pref
            new_node.nref = self.head
            new_node.pref = tail
            tail.nref = new_node
            self.head.pref = new_node
            self.head = new_node
    
    def addNode_AtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.nref = new_node
            new_node.pref = new_node
        else:
            tail = self.head.pref
            tail.nref = new_node
            new_node.pref = tail
            new_node.nref = self.head
            self.head.pref = new_node
    
    def deleteNode_AtBegin(self):
        if self.head is None:
            print("Node is empty!")
            return
        if self.head.nref == self.head:
            self.head = None
        else:
            tail = self.head.pref
            self.head = self.head.nref
            self.head.pref = tail
            tail.nref = self.head

cll1 = CircularDoublyLinkedList()
cll1.addNode_AtBegin(10)
cll1.addNode_AtBegin(20)
cll1.addNode_AtBegin(30)
cll1.print_LL()
