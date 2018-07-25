from first_class import FirstClass

class SecondClass(FirstClass):
    def __init__(self, name):
        self.name = name
        FirstClass().say_hello(self.name)
