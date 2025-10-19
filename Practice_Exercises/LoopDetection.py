'''
Given a linked list which might contain a loop. Implement an algorithm that returns the 
node at the beggining of the loop.

A -> B -> C-> D-> E-> C
'''



class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next 


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def peek(self):
        return self.head.data

    def add(self, n):
        if self.head == None:
            self.head = Node(n)
            return
        curr = self.head
        
        while curr.next is not None:
                curr = curr.next
        curr.next = Node(n)
        self.size += 1
        return

    def preppend(self,n):
        newhead = Node(n)
        newhead.next = self.head
        self.head = newhead
    
    def delete(self,n):
        if self.head.data == n:
            self.head = self.head.next 
            return
        curr = self.head 
        while curr.next is not None:
            if curr.next.data == n:
                curr.next = curr.next.next
                self.size -= 1
                return 

    def getsize(self):
        return self.size

    def print(self):
        curr = self.head

        while curr is not None:
            print(curr.data, end = '->')
            curr = curr.next
        
def LoopDetection(L):
    slow, fast = L.head.next,  L.head.next.next
    while fast.next.next is not None and fast is not None:
       
        if fast == slow:
            return fast.data
        slow, fast = slow.next , fast.next.next
    return None


if __name__ == '__main__':
    ll = LinkedList()
    ll.add('A')
    ll.add('B')
    ll.add('C')
    ll.add('D')
    ll.add('E')
    ll.head.next.next.next.next = ll.head.next.next
    ll.print()

    print(LoopDetection(ll))