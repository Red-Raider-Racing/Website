'''
author: Carson Spaniel
date: 10/27/23
'''
import requests
import json

url = 'https://sheetdb.io/api/v1/p6no685tantkk'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

#Insert Row
def insertRow(firstName, lastName, email, section):
    '''
    Function to insert details into the Google Sheet.
    '''
    data = {
        'data': [
            {
                'First Name': firstName.capitalize(),
                'Last Name': lastName.capitalize(),
                'Email': email,
                'Section': section.capitalize(),
            }
        ]
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 201:
        response_data = response.json()
        print(response_data)
    else:
        print(f"Request failed with status code {response.status_code}")
        raise Exception
    # row = [firstName,lastName, email, section] # Row to be inserted
    # sheet.insert_row(row,0) # Puts the row at index 0