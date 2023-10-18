'''
author: Carson Spaniel
date: 10/17/23

To run the tests:
    py manage.py collectstatic
    py manage.py test RRRApp.tests
'''

from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ValidationError
from unittest.mock import patch

from RRRApp.functions.email import *

class EmailTestCase(TestCase):
    '''
    All tests associated with email.py
    '''

    def test_formatMessage_pass(self):
        '''
        This one should pass by using correct values.
        '''

        name = "John Doe"
        email = "john.doe@example.com"
        message = "This is a test message."

        # Call the function with the test input
        formatted_message = formatMessage(name, email, message)

        # Check the expected output
        expected_message = f'This message is from {name} on {datetime.now().strftime("%A")} {datetime.now().strftime("%m/%d/%Y")} at {datetime.now().strftime("%I")}:{datetime.now().strftime("%M")} {datetime.now().strftime("%p")}:\n\n\n{message}\n\n\nTo respond to them, email them back at <a href="mailto:{email}">{email}</a>.'
        self.assertEqual(formatted_message, expected_message)

    def test_formatMessage_fail(self):
        '''
        This one should fail by using incorrect values.
        '''

        # Call the function with the test input
        formatted_message = formatMessage(None, None, None)

        # Check the expected output
        expected_message = False
        self.assertEqual(formatted_message, expected_message)


class IndexViewTestCase(TestCase):
    '''
    All tests associated with index in views.
    '''

    def test_index_view_GET(self):
        '''
        Testing to see if a GET request passes correctly and a template is returned.
        '''

        url = reverse('home') # More dynamic way to write 'home/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_view_POST(self):
        '''
        Testing to see if a POST request passes correctly.
        '''

        # Make a POST request to trigger the view
        response = self.client.post(reverse('home'), {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'subject': 'Test Subject',
            'message': 'Test message content'
        })
        
        # Check that the response is a redirect (status code 302)
        self.assertEqual(response.status_code, 302)

    @patch('RRRApp.views.emailMessage') # Mock the emailMessage function in RRRApp.views for testing
    def test_email_sending(self, mock_email_message):
        '''
        Testing to see if a is sent correctly.
        '''

        response = self.client.post(reverse('home'), {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'subject': 'Test Subject',
            'message': 'Test message content'
        })

        self.assertEqual(response.status_code, 302)

        # Now you can assert the redirect URL
        self.assertEqual(response.url, '/home/?success=1#message')

        # Check that the emailMessage function was called
        checkCall = mock_email_message.assert_called_once()
        self.assertEqual(checkCall, None)

    @patch('RRRApp.views.emailMessage')
    def test_backend_processing_error(self, mock_email_message):
        '''
        Simulating the email failing to send but make sure nothing breaks.
        '''

        # Set up the mock to raise an exception when called
        mock_email_message.side_effect = ValidationError('Email sending failed')

        response = self.client.post(reverse('home'), {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'subject': 'Test Subject',
            'message': 'Test message content'
        })

        # Check that the response is a redirect (status code 302)
        self.assertEqual(response.status_code, 302)

        # Now you can assert the redirect URL
        self.assertEqual(response.url, '/home/?success=0#message')