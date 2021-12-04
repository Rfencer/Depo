class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.thickness = 5/100

    def road_weight(self):
        return self._width*self._length*25*self.thickness


road = Road(1000, 50)


print(f'{round(road.road_weight())} kg')
