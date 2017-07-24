menu= [
    ['Regular', 2.08],
    ['Midgrade', 2.23],
    ['Premium', 2.36]  
]

def write_message(inventory, code, amount):
    message = 'Num, Type, Gallons, Price'
    for item in inventory:
        if item [1] == gas_name(code):
            item [2] = item [2] - amount[0]
        message += ('\n{0}, {1}, {2:.2f}, {3:.2f}'.format(item[0], item[1], item[2],item[3]))
    return message

def add_prepay(money, code, menu):
    for item in menu:
        if item[0] == gas_name(code):
            print('Gallons =', float(money / item[1]))
            gallons = float(money / item[1])
            return([gallons,money])

def add_payafter(code, menu, gallons):
    for item in menu:
        if item[0] == gas_name(code):
            print('Cash Due=',float(gallons * item[1]))
            money = float(gallons * item[1])
            return([gallons,money])

def gas_name(code):
    if code == '1':
        return('Regular')
    elif code == '2':
        return('Midgrade')
    elif code == '3':
        return('Premium')
    else:
        return ("Error Start Over")
 
def refill(inventory):
    message = 'Num, Type, Gallons, Price'
    for item in inventory:
            message += ('\n{0}, {1}, {2:.2f}, {3:.2f}'.format(item[0], item[1], float(5000.00),float(item[3])))
    return message

def revenue(text):
    total = 0
    for item in text:
        price = item
        total += float(price[3])
    return total

def choices(choice):
    """
    >>> choices('1')
    'Refilled Tanks'
    >>> choices('2')
    'Checked Revenue'
    >>> choices('3')
    'Opened Log'
    >>> choices('4')
    'Looked At Tank'
    """
    if choice == '1':
         return('Refilled Tanks')
    elif choice =='2':
        return('Checked Revenue')
    elif choice == '3':
        return('Opened Log')
    elif choice == '4':
        return('Looked At Tank')