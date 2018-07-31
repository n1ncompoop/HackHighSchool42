class Node(object):
    def __init__(self, data):
        if data == None:
            raise ValueError('Node must have data')
        self.data = data
        self.next = None
    
    @property
    def content(self):
        return self.data
    
    @content.setter
    def content(self, val):
        self.data = val
    
    @property
    def next(self):
        return self.next
    
    @next.setter
    def next(self, val):
        self.next = val