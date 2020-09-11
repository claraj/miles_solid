import unittest 
from unittest import TestCase
from unittest.mock import MagicMock, patch

import builtins
import importlib

from view import view_util, view
import view_model
from model.model import Vehicle

class TestView(TestCase):

    @patch('view.view_util.input_positive_float')
    @patch('builtins.input')
    def test_insert_one_vehicle(self, mock_input, mock_positive_float):

        """ Need to replace the ViewModel with a fake view model
        so the data is not sent to a real database. This test 
        cares that the update_one_vehicle is calling the increase_miles
        method in the view_model with the right data. 
        
        The two patch decorators: 
        Replace the input_positive_float with a mock function that returns
        a pre-configured value. Otherwise the test will stop and wait for input.
        
        Update one vehicle also uses the builtin input function, so replace
        that with a mock too, again, returning a pre-configured value.

        Patching replaces the parts of the program with mocks just for the 
        duration of this test. When this test is done (passes, fails, errors, whatever)
        the original methods/functions are restored. 
        
        """

        mock_input.return_value = 'Green Car'
        mock_positive_float.return_value = 3

        # re-import view here so when it imports other things, specfically the view_util
        # library, it will get the view_util library with the mock input_positive_float
        importlib.reload(view)

        # Make mock (fake, pretend) ViewModel with a mock insert method
        # We can make the mock here since it's not replacing any part of the 
        # program code - it's a self-contained mock object. Use this to figure 
        # out if the view calls the expected method with the correct data. 
        mock_view_model = MagicMock()
        mock_view_model.insert = MagicMock()

        # Give the new View the mock ViewModel
        test_view = view.View(mock_view_model)

        # The patched inputs will return 'Green Car' and 3 so the expected vehicle is like this,
        vehicle = Vehicle('Green Car', 3)

        # Call the method under test! 
        test_view.get_one_new_vehicle()

        # And assert the mock is called with the correct vehicle. 
        mock_view_model.insert.assert_called_with(vehicle)


    @patch('view.view_util.input_positive_float')
    @patch('builtins.input')
    def test_update_one_vehicle(self, mock_input, mock_positive_float):
        
        mock_input.return_value = 'Blue Car'
        mock_positive_float.return_value = 100

        # re-import view here so when it imports other things, specfically the view_util
        # library, it will get the view_util library with the mock input_positive_float
        importlib.reload(view)  # Re-import view to ensure it uses the mock imports
        
        # Make mock (fake, pretend) ViewModel with a mock insert method
        # We can make the mock here since it's not replacing any part of the 
        # program code - it's a self-contained mock object. Use this to figure 
        # out if the view calls the expected method with the correct data. 
        mock_view_model = MagicMock()
        mock_view_model.increase_miles = MagicMock()

        # Give the new View the mock ViewModel
        test_view = view.View(mock_view_model)

        # The patched inputs will return 'Blue Car' and 100 so the expected vehicle is like this,
        vehicle = Vehicle('Blue Car', 100)

        # Call the method under test! 
        test_view.update_one_vehicle()

        # And assert the mock is called with the correct vehicle. 
        mock_view_model.increase_miles.assert_called_with(vehicle, 100)