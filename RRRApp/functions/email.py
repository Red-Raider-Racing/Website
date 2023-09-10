from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
import asyncio

async def emailMessage(name, email, subject, message):
    message = formatMessage(name, message)

    try:
        # Use asyncio.to_thread to run the send_mail function in a separate thread
        await asyncio.to_thread(
            send_mail,
            subject,
            message,
            email,
            ['redraiderracingcode@outlook.com'],
            fail_silently=False,
        )
        return HttpResponse('Successful email sent.')
    except BadHeaderError:
        # Handle a BadHeaderError (e.g., invalid subject)
        return HttpResponse('Invalid header found.')
    except Exception as e:
        # Handle other exceptions (e.g., SMTP errors, connection issues)
        return HttpResponse(f'An error occurred: {str(e)}')

def formatMessage(name, message):
    message = f'This message is from {name}:\n\n"{message}"'
    print(message)
    return message