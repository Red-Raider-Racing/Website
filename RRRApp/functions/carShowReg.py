'''
author: Carson Spaniel
date: 10/27/23
'''
import requests
import json
from ..appSecrets import username, password

url = 'https://sheetdb.io/api/v1/0v2vn3ko7qafp'

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

    response = requests.post(url, data=json.dumps(data), headers=headers, auth=(username, password))

    if response.status_code != 201:
        print(f"Request failed with status code {response.status_code}")
        raise Exception