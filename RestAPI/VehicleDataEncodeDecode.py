import json

class Vehicle:
    def __init__(self, registration_number, year_of_production, passenger, mass):
        self.registration_number = registration_number
        self.year_of_production = year_of_production
        self.passenger = passenger
        self.mass = mass

class MyEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Vehicle):
            return w.__dict__
        else:
            return super().default(self, z)

class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_vehicle)

    def decode_vehicle(self, d):
        return Vehicle(**d)


if __name__ == '__main__':

    option = input('''What can I do for you?\n1 - produce a JSON string describing a vechicle\n2 - decode a JSON sting into data\nYour chioce: ''')

    if option == str(1):
        reg_no = input('Registration number: ')
        prod_year = int(input('Year of production: '))
        passangers = bool(input('Passenger [y/n]: '))
        mass_v = float(input('Vehicle mass: '))

        car = Vehicle(reg_no,prod_year,passangers,mass_v)
        print('Resulting JSON string is: \n'+json.dumps(car, cls = MyEncoder))
        print('Done')

    elif option == str(2):
        string = input('Enter vehicle JSON sting: ')#{"registration_number": "PC38927Z", "year_of_production": 2018, "passenger": false, "mass": 1543.2}
        car = json.loads(string, cls = MyDecoder)
        print(car.__dict__)
        print('Done')
    else:
        print('Choose one of available options.')
        option = input('''What can I do for you?\n1 - produce a JSON string describing a vechicle\n2 - decode a JSON sting into data\nYour chioce: ''')
