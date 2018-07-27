from johndough import Johndough
from minimoose import Minniemoose
from peterpenn import Peterpenn

if __name__ == "__main__":
    jd = Johndough()
    pp = Peterpenn()
    mm = Minniemoose()
    jd.run_play("crimp")
    jd.run_play("asdf")
    jd.run_play("jug")
    pp.run_play("crimp")
    pp.run_play("asdf")
    pp.run_play("jug")
    mm.run_play("crimp")
    mm.run_play("asdf")
    mm.run_play("jug")