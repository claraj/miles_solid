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
        except ValueError as e:
            print('Enter a number.')


def header(text):
    stars = len(text) * '*'
    print(f'\n{stars}\n{text}\n{stars}\n')


def show_vehicle_list(vehicles):
    for index, vehicle in enumerate(vehicles):
        print(f'{index + 1}. {vehicle}')