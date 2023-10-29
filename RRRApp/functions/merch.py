'''
author: Carson Spaniel
date: 10/29/23
'''

items = {
    0:'2023-24 Team T-Shirt',
    1:'2023-24 RRR Sticker',
    2:'Retired Team T-Shirts',
    }

def merchMessageFormat(name, item, size):
    if item == 0:
        inlineMessage = f'a {items[item]} in a size {size.upper()}'
    elif item == 2:
        inlineMessage = f'{items[item]} in a size {size.upper()}'
    else:
        inlineMessage = f'a {items[item]}'

    message = (
        f'{name} is wondering if we have {inlineMessage} available for purchase.'  # Message if the item has a size
    )
    return message, items[item]