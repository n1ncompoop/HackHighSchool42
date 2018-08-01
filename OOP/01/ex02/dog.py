from animal import Animal

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
    def speak(self):
        print("Woof")