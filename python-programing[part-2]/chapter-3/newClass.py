# python3 chapter-3/newClass.py

class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def start(self):
        print('name: ', self.name)
        print('color: ', self.color)
        print('Start the engine')


my_car = Car('Corolla', 'White')
my_car.start()