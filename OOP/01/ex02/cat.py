from animal import Animal

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
    def speak(self):
        print("Meow")