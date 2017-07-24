menu= [
    ['Regular', 2.08],
    ['Midgrade', 2.23],
    ['Premium', 2.36]  
]

def load_inventory():
    with open('tank.txt','r') as tank:
        tank.readline()
        str_inventory = tank.readlines()
    
    inventory = []
    for item in str_inventory:
        sub_list = item.split(', ')
        inventory.append([sub_list[0], (sub_list[1].strip()), float(sub_list[2].strip()), float(sub_list[3].strip())])
    return inventory

def close_inventory(inventory, code, amount):
    message = 'Num, Type, Gallons, Price'
    for item in inventory:
        if item [1] == gas_name(code):
            item [2] = item [2] - amount[0]
        message += ('\n{0}, {1}, {2:.2f}, {3:.2f}'.format(item[0], item[1], item[2],item[3]))
    with open("tank.txt",'w') as tank:
        tank.write(message)

def valid_pay():
     msg = """ How Will You Pay:
     \t1. Prepay
     \t2. Pay After
     """
     while True:
        payment = input(msg)
        if payment == '1' or payment == '2':
            return(payment)
        else:
            print('Error Try Again')

def addup(payment, code):
    if payment == '1':
        money = int(input('How Much You Buying?\n'))
        amount = add_prepay(money, code,menu)
    elif payment == '2':
        gallons = int(input('How Much Was Pumped?\n'))
        amount = add_payafter(code, menu, gallons)
    return amount

def add_prepay(money, code, menu):
    for item in menu:
        if item[0] == gas_name(code):
            print('Gallons =', round(money / item[1]))
            gallons = round(money / item[1])
            return([gallons,money])

def add_payafter(code, menu, gallons):
    for item in menu:
        if item[0] == gas_name(code):
            print('Cash Due=',round(gallons * item[1]))
            money = round(gallons * item[1])
            return([gallons,money])

def gas_name(code):
    if code == '1':
        return('Regular')
    elif code == '2':
        return('Midgrade')
    elif code == '3':
        return('Premium')
    else:
        print("Error Start Over")

def logit(code,amount,payment):
    with open("log.txt",'a') as file:
        if payment == '1' or payment == '2':
            file.write('{0}, {1}, {2}, {3:.2f}\n'.format(code,gas_name(code),amount[0],amount[1]))
        
def refill(inventory):
    message = 'Num, Type, Gallons, Price'
    for item in inventory:
            item [2] = float(5000.00)
            message += ('\n{0}, {1}, {2:.2f}, {3:.2f}'.format(item[0], item[1], item[2],item[3]))
    with open("tank.txt",'w') as tank:
        tank.write(message) 

def revenue():
    total = 0
    with open("log.txt","r") as file:
        file.readline()
        text = file.readlines()
        for item in text:
            price = item.split()
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