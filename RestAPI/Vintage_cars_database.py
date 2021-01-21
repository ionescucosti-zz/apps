import json
import sys

import requests


# http://localhost:3000/cars
def check_server(cid=None):
    global URL
    if len(sys.argv) not in [2, 3]:
        print('''Improper number of arguments: at least one is required and not more than two are allowed:
                - hhtp server's address (required)
                - port number(defaults to 80 if not specified)''')
        sys.exit(1)
    else:
        server = sys.argv[1]
        port = '3000'
        URL = server + ':' + port +'/cars/'
        if len(sys.argv) == 3:
            cid = sys.argv[2]
            URL = server + ':' + port + '/cars/' + cid
        try:
            reply = requests.get(URL)
        except requests.exceptions.Timeout:
            print('Connection timeout.')
            sys.exit(3)
        except Exception as e:
            print('Expception: ', e)
            sys.exit(4)
        else:
            if reply.status_code == requests.codes.ok:
                return True
            else:
                print('ID not in database.')
                return False

def print_menu():
    print('''
+-------------------------------+
|     Vintage Cars Database     |
+-------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit ''')

def read_user_choice():
    choice = input('Enter your choice (0..4): ')

    while not choice.isnumeric():
        print('Wrong choice!')
        choice = input('Enter your choice (0..4): ')

    while int(choice) not in [0, 1, 2, 3, 4]:
        print('Wrong choice!')
        choice = input('Enter your choice (0..4): ')

    return choice
#============ GET ===========
def print_header():
    # prints elegant cars table header;
    global key_names, key_widths;
    key_names = ["id", "brand", "model", "production_year", "convertible"]
    key_widths = [10, 15, 10, 20, 15]

    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()

def list_cars():
    # gets all cars' data from server and prints it;
    # if the database is empty prints diagnostic message instead;
    global key_names, key_widths, URL;
    reply = requests.get(URL)
    json = reply.json()

    if len(json) < 1:
        print('*** Database is empty ***')
        print()
    elif type(json) is list:
        print_header()
        for car in json:
            for (n, w) in zip(key_names, key_widths):
                print(str(car[n]).ljust(w), end='| ')
            print()
    elif type(json) is dict:
        print_header()
        if json:
            for (n, w) in zip(key_names, key_widths):
                print(str(json[n]).ljust(w), end='| ')
            print()

def print_car(car):
    pass
    # prints one car's data in a way that fits the header;
#============ POST ===========
def enter_id():
    # allows user to enter car's ID and checks if it's valid;
    # valid ID consists of digits only;
    # returns int or None (if user enters an empty line);
    id = input('Car ID (empty string to exit): ')
    if len(id) == 0:
        return None
    else:
        while not id.isdigit():
            print('ID must be digit')
            id = input('ID: ')
        return id

def name_is_valid(name):
    # checks if name (brand or model) is valid;
    # valid name is non-empty string containing
    # digits, letters and spaces;
    # returns True or False;
    if len(name) > 0 and all(x.isalpha() or x.isdigit() or x.isspace() for x in name):
        return True
    else:
        return False

def enter_production_year():
    # allows user to enter car's production year and checks if it's valid;
    # valid production year is an int from range 1900..2000;
    # returns int or None  (if user enters an empty line);
    while True:
        year = input('Car production year (empty string to exit): ')
        if len(year) == 0:
            return None
        elif year.isdigit() and int(year) >= 1900 and int(year) <= 2020:
            return int(year)

def enter_name(what):
    # allows user to enter car's name (brand or model) and checks if it's valid;
    # uses name_is_valid() to check the entered name;
    # returns string or None  (if user enters an empty line);
    # argument describes which of two names is entered currently ('brand' or 'model');
    while True:
        n = input('Car ' + what + '(empty string to exit): ')
        if len(n)==0:
            return None
        elif name_is_valid(n) is True:
            return n

def enter_convertible():
    # allows user to enter Yes/No answer determining if the car is convertible;
    # returns True, False or None  (if user enters an empty line);
    while True:
        convertible = input('Is this car convertible? [y/n] (empty string to exit): ')
        if len(convertible) == 0:
            return None
        elif convertible == 'y':
            return True
        elif convertible == 'n':
            return False

def input_car_data(with_id):
    # lets user enter car data;
    # argument determines if the car's ID is entered (True) or not (False);
    # returns None if user cancels the operation or a dictionary of the following structure:
    # {'id': int, 'brand': str, 'model': str, 'production_year': int, 'convertible': bool }
    if with_id is True:
        id = enter_id()
    else:
        id = with_id

    brand = enter_name('brand')
    model = enter_name('model')
    year = enter_production_year()
    convertible = enter_convertible()

    new_car = {'id': id,
               'brand': brand,
               'model': model,
               'production_year': year,
               'convertible': convertible}
    for x in new_car.values():
        if x == None:
            return x
            exit(0)
    print(new_car.values())
    print('To add: ' + json.dumps(new_car))
    return new_car


def add_car():
    # invokes input_car_data(True) to gather car's info and adds it to the database;
    h_content = {'Content-Type': 'application/json'}
    new_car = input_car_data(True)
    try:
        reply = requests.post('http://localhost:3000/cars', headers=h_content, data=json.dumps(new_car))
        print("Status = " + str(reply.status_code) + ': ' + repr(reply.text).split('\n')[0][1:21])
    except Exception as e:
        print(e)

#============ DELETE ===========
def delete_car():
    # asks user for car's ID and tries to delete it from database;
    global URL
    id = input('Enter car id to be deleted: ')
    URL = str(URL+id)
    print(URL)
    reply = requests.delete(URL)
    print('Status: '+str(reply.status_code)+':'+str(reply.text))

#============ PUT ===========
def update_car():
    # invokes enter_id() to get car's ID if the ID is present in the database;
    # invokes input_car_data(False) to gather new car's info and updates the database;
    global URL
    id = enter_id()
    url = URL+id
    h_content = {'Content-Type': 'application/json'}
    new_car = input_car_data(id)
    try:
        reply = requests.put(url, headers=h_content, data=json.dumps(new_car))
        print("Status = " + str(reply.status_code) + ': ' + repr(reply.text).split('\n')[0][1:21])
    except Exception as e:
        print(e)

while True:
    if not check_server():
        print("Server is not responding - quitting!")
        exit(1)
    print_menu()
    choice = read_user_choice()
    if choice == '0':
        print("Bye!")
        exit(0)
    elif choice == '1':
        list_cars()
    elif choice == '2':
        add_car()
    elif choice == '3':
        delete_car()
    elif choice == '4':
        update_car()