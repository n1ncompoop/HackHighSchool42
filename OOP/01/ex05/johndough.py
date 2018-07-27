from player import Player

class Johndough(Player):
    def __init__(self):
        Player.__init__(self) 
    def run_play(self, play):
        self.play = play
        if play in self.playbook:
            if play == "crimp":
                print("Oh! a nasty slip for John")
            elif play == "jug":
                print("An easy swing to the jug fof Mr.Dough!")
            elif play == "dyno":
                print("Look at John flying with grace!")
            elif play == "sloper":
                print("A slippery slope for John")
        else:
            print("John Dough? more like John Doh!")
