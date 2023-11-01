'''
author: Carson Spaniel
date: 10/27/23
'''
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#Authorize the API
scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]
file_name = 'client_key.json'
# creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
# client = gspread.authorize(creds)

#Fetch the sheet
# sheet = client.open('Car Show Registration').sheet1
sheet = None

#Insert Row
def insertRow(firstName, lastName, email, section):
    '''
    Function to insert details into the Google Sheet.
    '''
    row = [firstName,lastName, email, section] # Row to be inserted
    sheet.insert_row(row,0) # Puts the row at index 0