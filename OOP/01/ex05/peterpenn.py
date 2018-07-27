from player import Player

class Peterpenn(Player):
    def __init__(self):
        Player.__init__(self)
    def run_play(self, play):
        self.play = play
        if play in self.playbook:
            if play == "crimp":
                print("Made that look like magic!")
            elif play == "jug":
                print("Oof, a miss for Peter")
            elif play == "dyno":
                print("It's easier with wings, but we don't discriminate")
            elif play == "sloper":
                print("A sad yet magestic fall")
        else:
            print("I guess brain size does matter!")
