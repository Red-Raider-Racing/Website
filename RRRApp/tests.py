'''
author: Carson Spaniel
date: 10/17/23

To run the tests: 
py manage.py test RRRApp.tests
'''

from django.test import TestCase
from RRRApp.functions.email import *

class EmailTests(TestCase):
    '''
    All tests associated with email.py
    '''

    def test_formatMessage(self):
        print("\nTesting formatMessage...")

        name = "John Doe"
        email = "john.doe@example.com"
        message = "This is a test message."

        # Call the function with the test input
        formatted_message = formatMessage(name, email, message)

        # Check the expected output
        expected_message = f'This message is from {name} on {datetime.now().strftime("%A")} {datetime.now().strftime("%m/%d/%Y")} at {datetime.now().strftime("%I")}:{datetime.now().strftime("%M")} {datetime.now().strftime("%p")}:\n\n\n{message}\n\n\nTo respond to them, email them back at <a href="mailto:{email}">{email}</a>.'
        self.assertEqual(formatted_message, expected_message)