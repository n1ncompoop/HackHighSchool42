from animal import Animal
from cat import Cat
from dog import Dog

if __name__ == "__main__":
    an = Animal()
    cat = Cat()
    dog = Dog()
    cat.speak()
    dog.speak()
    an.speak()
    an.sleep()
    dog.sleep()
    cat.sleep()