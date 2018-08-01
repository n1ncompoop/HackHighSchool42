class Node:
    def __init__(self, value, next = None):
        self.data = value
        self.next = next

class Stack:
    def __init__(self):
        self.data = None
        self.next = None
    
    def isEmpty(self):
        if self.data == None:
            if self.next = None:
                return None
        return self

    
    def push(self, data):
        node = Node(data)
        node.next = self

    
    def pop(self):
        head = self
        while self.next != None:
            prev = self
            self = self.next
        prev.next = None
        return head
        
    
    def peek(self):
        while self.next != None:
            self = self.next
        return self.data
    
    def size(self):
        i = 0
        while self.next != None:
            self = self.next
            i += 1
        return i
    
    def __str__(self):
        string = ""
        while self.next != None:
            string += self.next
            self = self.next
        print(string)
