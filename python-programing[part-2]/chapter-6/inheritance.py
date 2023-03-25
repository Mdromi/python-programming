# python3 chapter-6/inheritance.py

class Vehicle:
    """Base Class for all vehicles"""

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
    
    def drive(self):
        print('Driving', self.manufacturer, self.color)
    
    def turn(self, direction):
        print('Turning', self.name, 'to', direction)
    
    def brake(self):
        print(self.name, 'is stopping')

class Car(Vehicle):
    """Car class"""

    def __init__(self, name, manufacturer, color, year):
        print('Creating a car')
        super().__init__(name, manufacturer, color)
        self.year = year
        self.wheels = 4

    def change_gear(self, gear_name):
        """Method for changing gear"""
        print(self.name, 'is changing gear to', gear_name)


if __name__ == '__main__':
    c = Car('Mustang 5.0', 'ford', 'Red', 2018)
    c.drive()
    c.brake()
    c.turn('left')
    c.change_gear('P')
    print(c.name, c.year, c.wheels)


# if __name__ == '__main__':
#     v1 = Vehicle('Function 119 EX', 'Walton', 'Black')
#     v2 = Vehicle('Softail Delux', 'Harley', 'Blue')
#     v3 = Vehicle('Mustang 5.0', 'ford', 'Red')

#     v1.drive()
#     v2.drive()
#     v3.drive()

#     v1.turn('left')
#     v2.turn('right')

#     v1.brake()
#     v2.brake()
#     v3.brake()