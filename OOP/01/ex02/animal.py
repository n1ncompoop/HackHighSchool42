class Animal():
    def __init__(self):
        print("Making a {}".format(self.__class__.__name__))
    def speak(self):
        pass
    def sleep(self):
        print("Zzzz...")