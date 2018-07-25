import sys

class FirstClass():
    def __init__(self):
        pass
    def say_hello(self, name):
        self.name = name
        print("Method {} in {} is called".format(sys._getframe().f_code.co_name, self.__class__.__name__))
        print("Hello {}!".format(self.name))
