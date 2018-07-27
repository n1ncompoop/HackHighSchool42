from player import Player

class Minniemoose(Player):
    def __init__(self):
        Player.__init__(self)
    def run_play(self, play):
        self.play = play
        if play in self.playbook:
            if play == "crimp":
                print("What an agile moose!")
            elif play == "jug":
                print("A snug grip for Minnie!")
            elif play == "dyno":
                print("Just a few pounds too heavy for Ms.Moose")
            elif play == "sloper":
                print("Oh! so close for those mini hands")
        else:
            print("Look's like she's stumped with this problem")
