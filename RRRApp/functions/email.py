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
    # Format the date
    formatted_date = carShowLoc.date.strftime("%B %d, %Y")

    message = f'''
        <!DOCTYPE html>
        <html>
        <body style="max-width: 1200px; margin: 0 auto; padding: 20px; background-color: #f4f4f4; font-family: Arial, sans-serif;  width: 100%;">
            <span class="header" style="text-align: center; margin: 0 auto; display: block; width: 100%;">
                <h1 style="color: #333; font-size: 24px;">Thank you for registering for the {carShowLoc.year} Red Raider Racing Car Show!</h1>
                <h2 style="color: #333; font-size: 20px; text-align: center; max-width: 600px; margin: 0 auto;">{formatted_date} at {carShowLoc.location_name}</h2>
            </span>
            <span style="margin: 0 auto; display: block; width: 100%;">
                <p style="color: #555; font-size: 16px; max-width: 600px; margin: 0 auto;">You are currently registered under <strong>{firstName.capitalize()} {lastName.capitalize()}</strong> for the <strong>{section.capitalize()}</strong> section.</p>
                <p style="color: #555; font-size: 16px; max-width: 600px; margin: 0 auto;">You must pay to enter the car show. Pay now for a discounted price, or you can pay at the entrance.</p>
                <a href="{carShowLoc.email_preregister_payment_link}" style="display: block; background-color: #b70102; color: #fff; padding: 10px 20px; text-align: center; margin: 20px auto; border-radius: 5px; text-decoration: none; max-width: 600px;">
                    <h2 class="payNow" style="color: #ffffff; margin: 10px auto;">Pay Now</h2>
                </a>
            </span>
            <span class="footer" style="background-color: #ddd; text-align: center; margin: 0 auto; display: block; width: 100%;">
                <h2 style="color: #333; font-size: 20px;">Red Raider Racing</h2>
                <p style="color: #555; font-size: 16px;">If anything looks wrong or you are having trouble paying, please <a href="mailto:{mainEmail}" style="text-decoration: none; color: #b70102;">Contact Us</a> and we can happily assist you!</p>
            </span>
        </body>
        </html>
        '''

    return message