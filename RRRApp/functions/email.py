'''
author: Carson Spaniel
date: 9/9/23
'''

from django.core.mail import send_mail
from datetime import datetime

def emailMessage(subject, message, fromEmail, toEmail):
    '''
    Used to take the inputs and send an email to our email.
        - currently using 'redraiderracingcode@outlook.com' for testing.\n
    Returns None.
    '''
    if message:
        send_mail(
            subject,
            message,
            fromEmail, # Send email from
            [toEmail], # Send email to
            # fail_silently=False, # We don't want it to fail silently that way it raises an error
        )
    else:
        raise Exception

def formatMessage(name, email, subject, message):
    '''
    Used to format the message how ever you want.\n
    Returns the full message to send in the email.
    '''
    if name and email and message:
        day_of_week, date, email_link = emailDate(email, subject)
        
        fullMessage = (
            f'This message is from {name} on {day_of_week} {date} at '  # Date and time information
            f'{datetime.now().strftime("%I")}:{datetime.now().strftime("%M")} '  # Hour and minute
            f'{datetime.now().strftime("%p")}:\n\n\n{message}\n\n\nTo respond to them, '  # AM or PM and message
            f'email them back at {email_link}.'  # Email link
        )

        return fullMessage
    
    else:
        return False
    
def emailDate(email, subject):
    day_of_week = datetime.now().strftime('%A') # Full day name (e.g., "Monday")
    date = datetime.now().strftime('%m/%d/%Y') # In the format MM/DD/YYYY

    email_link = f'<a href="mailto:{email}?subject=RE: {subject}">{email}</a>' # Makes a clickable link in the email
    return day_of_week, date, email_link
    
def carShowEmailFormat(firstName, lastName, email, section, carShowLoc, mainEmail):
    message = (
        f'{firstName},\n'
        f'<strong>Thank you for registering for the {carShowLoc.year} Red Raider Racing Car Show!</strong>\n\n'
        f'The car show will take place at <strong>{carShowLoc.location_name}</strong> on <strong>{carShowLoc.date}</strong>.'
        f'<strong>You must pay to enter the car show</strong>. You can pay now for a discounted price, or you can pay at the gate.\n\n'
        f'<a href="{carShowLoc.email_preregister_payment_link}"><strong>Preregister link</strong></a>\n\n'
        f'Currently you are registered under "{firstName} {lastName}" for the {section} section.'
        f' If anything looks wrong or you are having trouble paying, please <a href="mailto:{mainEmail}">Contact Us</a> and we can happily assist you!'
    )
    return message