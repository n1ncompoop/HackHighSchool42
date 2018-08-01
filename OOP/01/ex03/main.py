from greeter import Greeter
from insult_comic import Insult

if __name__ == "__main__":
    gr = Greeter()
    ins = Insult()
    gr.speak("Jake")
    ins.speak("Mike")