from building import Building

class Campus(Building):
    def __init__(self):
        self.buildings = []
        self.num_buildings = 0
        self.capacity = 0
    def get_info(self):
        print("The campus has {} building(s) with a combined capacity of {} people".format(self.num_buildings, self.capacity))
    def add_building(self, asdf):
        self.buildings.append(asdf.name)
        self.num_buildings += 1
        self.capacity += asdf.capacity
