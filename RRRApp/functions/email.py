'''
author: Carson Spaniel
date: 9/9/23
'''

from django.core.mail import send_mail
from datetime import datetime

def emailMessage(name, email, subject, message):
    '''
    Used to take the inputs and send an email to our email.
        - currently using 'redraiderracingcode@outlook.com' for testing.\n
    Returns None.
    '''
    message = formatMessage(name,email,message)
    send_mail(
        subject,
        message,
        'redraiderracing@website.admin', # Send email from
        ['redraiderracingcode@outlook.com'], # Send email to
        fail_silently=False, # We don't want it to fail silently that way it raises an error
    )

def formatMessage(name, email, message):
    '''
    Used to format the message how ever you want.\n
    Returns the full message to send in the email.
    '''
    day_of_week = datetime.now().strftime('%A') # Full day name (e.g., "Monday")
    date = datetime.now().strftime('%m/%d/%Y') # In the format MM/DD/YYYY

    email_link = f'<a href="mailto:{email}">{email}</a>' # Makes a clickable link in the email
    
    message = (
        f'This message is from {name} on {day_of_week} {date} at '  # Date and time information
        f'{datetime.now().strftime("%I")}:{datetime.now().strftime("%M")} '  # Hour and minute
        f'{datetime.now().strftime("%p")}:\n\n\n{message}\n\n\nTo respond to them, '  # AM or PM and message
        f'email them back at {email_link}.'  # Email link
    )

    return message 