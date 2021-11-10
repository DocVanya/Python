class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Новая машина: {self.name} Цвет {self.color} Машина полицейская - {self.is_police}')

    def go(self):
        print(f'{self.name}: Машина поехала')

    def stop(self):
        print(f'{self.name}: Машина остановилась')

    def turn(self, direction):
        print(f'{self.name}: Машина повернула {"налево" if direction == 0 else "направо" }')

    def show_speed(self):
        print(f'{self.name}: Скорость машины - {self.speed}')


class WorkCar(Car):

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля - {self.speed} - Превышение скорости!'\
            if self.speed > 40 else f'{self.name}: Скорость автомобиля - {self.speed}'


class SportCar(Car):
    def show_speed(self):
        return f'{self.name}: Скорость автомобиля - {self.speed} - Превышение скорости!'\
            if self.speed > 80 else f'{self.name}: Скорость автомобиля - {self.speed}'


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = PoliceCar('ДПС', 'черный', 80)
police_car.go()
police_car.turn(1)
police_car.stop()
sport_car = SportCar('Ferrary', 'red', 300)
sport_car.show_speed()
