class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} is moving')

    def stop(self):
        print(f'{self.name} is stopped')

    def turn(self, direction):
        turn_tup = ('Right', 'Left')
        if direction.title() in turn_tup:
            print(f'{self.name} is turning {direction.title()}')
        else:
            print('Turn not possible')

    def show_speed(self):
        print(f'{self.name} is moving at {self.speed} km/h')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} going too fast!!: {self.speed} km/h')
        else:
            print(f'{self.name} speed is {self.speed} km/h')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} going too fast!!: {self.speed} km/h')
        else:
            print(f'{self.name} speed is {self.speed} km/h')


class SportCar(Car):
    def show_speed(self):
        if self.speed < 100:
            print(f'{self.name} accelerate man!! speed is: {self.speed} km/h')
        else:
            print(f'{self.name} keep accelerating man!! speed is {self.speed} km/h')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


town_car1 = TownCar(70, 'black', 'Town Car1')
town_car2 = TownCar(50, 'black', 'Town Car2')
work_car1 = WorkCar(70, 'black', 'Work Car1')
work_car2 = WorkCar(30, 'black', 'Work Car2')
sport_car1 = SportCar(70, 'black', 'Sport Car1')
sport_car2 = SportCar(120, 'black', 'Sport Car2')
police_car = PoliceCar(70, 'black', 'Police Car')

car_list = [town_car1, town_car2, work_car1,work_car2, sport_car1, sport_car2, police_car]

for car in car_list:
    car.show_speed()
    print(f'{car.name} is police - {car.is_police}')
    car.go()
    car.stop()
    car.turn('Right')
    car.turn('left')
    car.turn('blabla')
    print('\n')

