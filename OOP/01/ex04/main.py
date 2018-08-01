from building import Building
from campus import Campus

if __name__ == "__main__":
    bd = Building("Maths", 25)
    bd2 = Building("Science", 17)

    bd.get_info()
    bd2.get_info()

    cp = Campus()

    cp.add_building(bd)
    cp.add_building(bd2)
    
    cp.get_info()

