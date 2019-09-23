import sqlite3

db_url = 'miles.db'   # Assumes the table miles have already been created.

"""
Before running this code, ensure that miles.db exists and contains the miles table
If not, create expected miles table with 
create table miles (vehicle text, type text, total_miles float);
"""

class MileageError(Exception):
    pass


def add_miles(vehicle, new_miles):
    '''If the vehicle is in the database, increment the number of miles by new_miles
    If the vehicle is not in the database, add the vehicle and set the number of miles to new_miles
    If the vehicle is None or new_miles is not a positive number, raise MileageError
    '''

    if not vehicle:
        raise MileageError('Provide a vehicle name')
    if not isinstance(new_miles, (int, float)) or new_miles < 0:
        raise MileageError('Provide a positive number for new miles')

    with sqlite3.connect(db_url) as conn:
        # Attempt to update miles
        rows_mod = conn.execute('UPDATE MILES SET total_miles = total_miles + ? WHERE vehicle = ?', (new_miles, vehicle))
        if rows_mod.rowcount == 0:
            # If update is not made, vehicle is not yet in DB. Insert new vehicle
            conn.execute('INSERT INTO MILES VALUES (?, ?)', (vehicle, new_miles))
    conn.close()


def main():
    while True:
        vehicle = input('Enter vehicle name or enter to quit: ')
        if not vehicle:
            break
        miles = float(input(f'Enter new miles for {vehicle}: ')) ## TODO input validation

        add_miles(vehicle, miles)


if __name__ == '__main__':
    main()
