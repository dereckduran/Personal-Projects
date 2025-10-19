class Node(data):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(head: Node):
    def __init__(self,head):
        self.head = head


def Reverse(head: LinkedList):
    curr = head
    while curr: