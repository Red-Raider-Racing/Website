'''
author: Carson Spaniel
date: 9/9/23
'''

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from datetime import datetime

def emailMessage(name, email, subject, message):
    '''
    Used to take the inputs and send an email to our email.
        - currently using 'redraiderracingcode@outlook.com' for testing.
    '''

    message = formatMessage(name,message)
    try:
        send_mail(
            subject,
            message,
            email,
            ['redraiderracingcode@outlook.com'],
            fail_silently=False,
        )
        return HttpResponse('Success.')
    except BadHeaderError:
        # Handle a BadHeaderError (e.g., invalid subject)
        return HttpResponse('Invalid header found.')
    except Exception as e:
        # Handle other exceptions (e.g., SMTP errors, connection issues)
        return HttpResponse(f'An error occurred: {str(e)}')

def formatMessage(name, message):
    '''
    Used to format the message.
    '''
    message = f'This message is from redraiderracing.com from {name} at {datetime.now().strftime("%H:%M:%S")}:\n\n{message}'
    print(message)
    return message 

# formatMessage("Carson Spaniel","I would love to join the team. How can I start getting involved? \nThank you,\nCarson Spaniel")