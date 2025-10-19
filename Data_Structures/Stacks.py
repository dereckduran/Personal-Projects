from email import header
from logging import NullHandler
class Node:
        def __init__(self, data, next = None):
            self.data = data
            self.next = next

class Stack:

    def __init__(self):
        self.head = None

    def push(self, data):
        if self.isEmpty():
            self.head = Node(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head = node
       

    def pop(self):
        if self.isEmpty():
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            
            return data
    def isEmpty(self):
        return self.head == None
    
    def peek(self):
        if self.isEmpty(): return None
        else: return self.head.data
    
    def display(self):
        iternode = self.head
        if self.isEmpty():
            print("Stack Underflow")
          
        else:
              
            while(iternode != None):
                  
                print(iternode.data,"->",end = " ")
                iternode = iternode.next
            return

def ValidParenthesis(par):
    hash = {')':'(', ']':'[', '}':'{'}
    stack = Stack()
    for box in par:
        
        if box in hash.values():
            stack.push(box)
        elif box in hash.keys():
            if hash[box] != stack.pop():
                print(hash[box])
                return False
        else:
            return False
    print(stack)
    return stack.isEmpty()

#print(ValidParenthesis('()[]'))

'''
Write a program to sort a stack such that the smallest items are on top. 
You can use an additional temporary stack, but you may not copy elements into any other data structure (such as an array).

The stack supports the following operations : push, pop, peek, isEmpty.

Input and output are both stacks

Input : [34, 3, 31, 98, 92, 23]
Output : [3, 23, 31, 34, 92, 98]

Input : [3, 5, 1, 4, 2, 8]
Output : [1, 2, 3, 4, 5, 8]
'''
nums = [3, 5, 1, 4, 2, 8]
stack = Stack()
for i in nums[:]:
    stack.push(i)

def sortStack(stack: Stack):
    tempstack = Stack()

    while stack.isEmpty() == False:
        temp = stack.pop()
        
        while tempstack.isEmpty() == False and tempstack.peek() >= temp:
            popped = tempstack.pop()
            stack.push(popped)

        tempstack.push(temp)

    tempstack.display()



print(sortStack(stack))