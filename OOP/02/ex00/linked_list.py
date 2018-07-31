from node import Node

class LinkedList(object):
    def __init__(self):
        self.head = None

    @property
    def head(self):
        return(self.head)
    
    @head.setter
    def head(self, node):
        self.head = node

    def isEmpty(self):
        return self.head == None
    
    def add_head(self, val):
        nod = Node(val)
        if self.isEmpty():
            nod.next = None
            self.head = nod
        else:
            nod.next = self.head
            self.head = nod
            #can change to self.head(nod)?
    
    def add_tail(self, val):
        nod = Node(val)
        if self.isEmpty():
            nod.next = None
            self.head = nod
        else:
            nod.next = None
            self.next = nod
    
    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next
    
    def __str__(self):
        if self.isEmpty():
            pass
        else:
            string = ""
            while self.head != None:
                string += self.data
                self.head = self.next
            print(string)
    
    @property
    def size(self1):
        if self.isEmpty():
            return (0)
        else:
            i = 0
            while self.head != None:
                i += 1
                self.head = self.next
            return i
    
    def remove_first(self, val):
        if self.isEmpty():
            return False
        elif self.data == val:
            self.head = self.next
                return True
        else:
            while self.head != None:
                cur = self.head
                self.head = self.next
                if self.data == val:
                    cur.next = self.next
                    return True
            return False
    
    def has_cycle(self):
        s = set()
        tmp = self.head
        while tmp:
            if tmp in s:
                return True
            s.add(tmp)
            tmp = tmp.next
        return False
    
    def sort_asc(self):
        tmp = self.head
        nxt = tmp.next
        while tmp:
            while nxt:
                if tmp.data > nxt.data:
                    tmp.next = nxt.next
                    nxt.next = tmp
                    tmp = nxt
                    nxt = tmp.next
                else:
                    nxt = nxt.next
            tmp = tmp.next
            

        