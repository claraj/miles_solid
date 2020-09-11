"""
Input and validation utilities
"""

def input_positive_float(question):
    while True:
        try:
            number = float(input(question))
            if number < 0:
                print('Enter a positive number')
            else:
                return number 
        except ValueError:
            print('Enter a number.')


def header(text):
    stars = len(text) * '*'
    print(f'\n{stars}\n{text}\n{stars}\n')


def show_vehicle_list(vehicles):

    print(f'{"Name":<20}  {"Miles":<20}')
    print('-' * 40)
    for vehicle in vehicles:
        print(f'{vehicle.name:<20}  {vehicle.miles:<20}')