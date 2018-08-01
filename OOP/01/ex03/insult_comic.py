class Insult():
    def __init__(self):
        pass
    def speak(self, name):
        self.name = name
        print("Hello {} you knobhead!".format(name))