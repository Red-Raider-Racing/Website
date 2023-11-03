'''
author: Carson Spaniel
date: 10/29/23
'''

def merchMessageFormat(name, item, size):
    if size:
        inlineMessage = f'a {item} in a size {size.upper()}'
    else:
        inlineMessage = f'a {item}'

    message = (
        f'{name} is wondering if we have {inlineMessage} available for purchase.'  # Message if the item has a size
    )
    return message