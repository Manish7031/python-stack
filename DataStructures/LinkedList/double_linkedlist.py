## double LL

class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class doubleLinkedList:
    def __init__(self):
        self.head = None
    
    def print_LL(self):
        if self.head is None:
            print("Double Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "->", end=" ")
                n = n.nref

    def print_LL_reverse(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print("\nReverse print=========> ",n.data, "->", end=" ")
                n = n.pref

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty")
    
    def addNode_AtBegin(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
    
    def addNode_AtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def addNode_After(self, data, x):
        if self.head is None:
            print("Linked List is empty !")
        else:
            n =  self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                    print("Node is not present in the Linked List")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node
        

    def addNode_Before(self, data, x):
        if self.head is None:
            print("Linked List is empty !")
        else:
            n =  self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
                if n is None:
                    print("Node is not present in the Linked List")
                else:
                    new_node = Node(data)
                    new_node.nref = n
                    new_node.pref = n.pref
                    if n.pref is not None:
                        n.pref.nref = new_node
                    else:
                        self.head = new_node
                    n.pref = new_node

    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty now!")
            return
        if self.head.nref is None:
            self.head = None
            print("node is deleted")
        else:
            self.head = self.head.nref
            self.head.pref = None
    
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty now!")
            return
        if self.head.nref is None:
            self.head = None
            print("node is deleted")
        else:
            n= self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None
    
    def delete_by_value(self, x):
        if self.head is None:
            print("Linked List is empty now!")
            return
        if self.head.nref is None:
            if x == self.head.data:
                self.head = None
            else:
                print(x, "Node is not present in the Linked List")
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if x== n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data==x:
                n.pref.nref = None
            else:
                print("Node is not present in the Linked List")



dl1 = doubleLinkedList()
#dl1.insert_empty(100)
dl1.addNode_AtBegin(50)
dl1.addNode_AtBegin(25)
dl1.addNode_AtEnd(75)
dl1.addNode_Before(60, 50)
dl1.addNode_After(80, 75)
dl1.print_LL()
#dl1.print_LL_reverse()