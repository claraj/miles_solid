import sqlite3
import unittest
from unittest import TestCase

from sql_database import database 

from model.model import Vehicle

from exceptions.mileage_error import MileageError


class TestMileageDB(TestCase):

    test_db_url = 'test_miles.db'

    """
    Before running these test, create test_miles.db
    Create expected miles table
    create table miles (vehicle text, total_miles float);
    """

    # The name of this method is important - the test runner will look for it
    def setUp(self):
        database.db = self.test_db_url


        # drop everything from the DB to always start with an empty database
        with sqlite3.connect(self.test_db_url) as conn:
            conn.execute('DROP TABLE IF EXISTS miles')
        conn.close()

        with sqlite3.connect(self.test_db_url) as conn:
            conn.execute('CREATE TABLE MILES (vehicle TEXT UNIQUE NOT NULL, total_miles FLOAT)')
        conn.close()

        self.db = database.SQLVehicleDB()
    

    def test_add_new_vehicle(self):
        v1 = Vehicle('Blue Car', 100)
        self.db.insert(v1)
        expected = { 'Blue Car' : 100 }
        self.compare_db_to_expected(expected)

        v2 = Vehicle('Green Car', 50)
        self.db.insert(v2)
        expected = { 'Blue Car': 100, 'Green Car': 50 }
        self.compare_db_to_expected(expected)

        v3 = Vehicle('Red Car', 0)
        self.db.insert(v3)
        expected = { 'Blue Car': 100, 'Green Car': 50, 'Red Car': 0}
        self.compare_db_to_expected(expected)


    def test_will_not_add_duplicate_vehicle(self):
        v1 = Vehicle('Blue Car', 100)
        self.db.insert(v1)
        expected = { 'Blue Car' : 100 }
        
        self.compare_db_to_expected(expected)

        with self.assertRaises(MileageError):
            v2 = Vehicle('Blue Car', 50)
            self.db.insert(v2)
        
        expected = { 'Blue Car': 100 }   # Will not modify DB
        self.compare_db_to_expected(expected)


    def test_increase_miles_for_vehicle(self):
        # v1 = Vehicle('Blue Car', 100)
        # self.db.insert(v1)
        # expected = { 'Blue Car' : 100 }
        # self.compare_db_to_expected(expected)

        # self.db.increase_miles(v1, 50)
        # expected['Blue Car'] = 100 + 50
        # self.compare_db_to_expected(expected)


        v1 = Vehicle('Pie', 0)
        self.db.insert(v1)
        self.db.increase_miles(v1, 30)
        


    def test_error_increase_miles_for_vehicle_not_in_db(self):
        v1 = Vehicle('Purple Car', 100)
        self.db.insert(v1)
        expected = { 'Purple Car' : 100 }

        v_not_in_db = Vehicle('Blue Car')

        with self.assertRaises(MileageError):
            self.db.increase_miles(v_not_in_db, 50)
            
        self.compare_db_to_expected(expected)


    def test_add_new_vehicle_no_vehicle(self):
        v_no_name = Vehicle(None)
        with self.assertRaises(MileageError):
            self.db.insert(v_no_name)


    def test_add_new_vehicle_invalid_new_miles(self):

        v_negative = Vehicle('Car', -100)
        v_alpha = Vehicle('Car', 'abc')

        with self.assertRaises(MileageError):
            self.db.insert(v_negative)
        with self.assertRaises(MileageError):
            self.db.insert(v_alpha)


    def test_increase_miles_no_vehicle(self):
        v_no_name = Vehicle(None)
        with self.assertRaises(MileageError):
            self.db.increase_miles(v_no_name, 100)


    def test_increase_miles_invalid_new_miles(self):

        v_negative = Vehicle('Green Car', -100)
        v_alpha = Vehicle('Green Car', 'abc')

        v1 = Vehicle('Green Car', 100)
        self.db.insert(v1)
        
        with self.assertRaises(MileageError):
            self.db.increase_miles(v_negative, -100)
        with self.assertRaises(MileageError):
            self.db.increase_miles(v_alpha, 'pizza')


    # This is not a test method, instead, it's used by the test methods
    def compare_db_to_expected(self, expected):

        conn = sqlite3.connect(self.test_db_url)
        all_data = conn.execute('SELECT * FROM MILES').fetchall()

        # Same rows in DB as entries in expected dictionary
        self.assertEqual(len(expected.keys()), len(all_data))

        for row in all_data:
            # Vehicle exists, and mileage is correct
            self.assertIn(row[0], expected.keys())
            self.assertEqual(expected[row[0]], row[1])

        conn.close()


if __name__ == '__main__':
    unittest.main()