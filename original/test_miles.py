import sqlite3
import unittest
from unittest import TestCase

import miles
from miles import MileageError


class TestMileageDB(TestCase):

    test_db_url = 'test_miles.db'

    """
    Before running these test, create test_miles.db
    Create expected miles table
    create table miles (vehicle text, type text, total_miles float);
    """

    # The name of this method is important - the test runner will look for it
    def setUp(self):
        # Overwrite the mileage
        miles.db_url = self.test_db_url
        # drop everything from the DB to always start with an empty database
        with sqlite3.connect(self.test_db_url) as conn:
            conn.execute('DELETE FROM miles')
        conn.close()


    def test_add_new_vehicle(self):
        miles.add_miles('Blue Car', 100)
        expected = { 'Blue Car': 100 }
        self.compare_db_to_expected(expected)

        miles.add_miles('Green Car', 50)
        expected['Green Car'] = 50
        self.compare_db_to_expected(expected)


    def test_increase_miles_for_vehicle(self):
        miles.add_miles('Red Car', 100)
        expected = { 'Red Car': 100 }
        self.compare_db_to_expected(expected)

        miles.add_miles('Red Car', 50)
        expected['Red Car'] = 100 + 50
        self.compare_db_to_expected(expected)


    def test_add_new_vehicle_no_vehicle(self):
        with self.assertRaises(Exception):
            mileage.addMiles(None, 100)


    def test_add_new_vehicle_invalid_new_miles(self):
        with self.assertRaises(MileageError):
            miles.add_miles('Car', -100)
        with self.assertRaises(MileageError):
            miles.add_miles('Car', 'abc')
        with self.assertRaises(MileageError):
            miles.add_miles('Car', '12.def')


    # This is not a test method, instead, it's used by the test methods
    def compare_db_to_expected(self, expected):

        conn = sqlite3.connect(self.test_db_url)
        cursor = conn.cursor()
        all_data = cursor.execute('SELECT * FROM MILES').fetchall()

        # Same rows in DB as entries in expected dictionary
        self.assertEqual(len(expected.keys()), len(all_data))

        for row in all_data:
            # Vehicle exists, and mileage is correct
            self.assertIn(row[0], expected.keys())
            self.assertEqual(expected[row[0]], row[1])

        conn.close()


if __name__ == '__main__':
    unittest.main()