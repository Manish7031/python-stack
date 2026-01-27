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
                print(sh.data)
                sh = sh.ref

ll1 = LinkedList()
ll1.print_LL()