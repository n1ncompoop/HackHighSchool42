class Building():
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
    def get_info(self):
        print('Building "{}" can HODL {} people'.format(self.name, self.capacity))