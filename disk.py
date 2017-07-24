from gascore import *

def load_inventory():
    with open('tank.txt','r') as tank:
        tank.readline()
        items = []
        for line in tank.readlines():
            items.append(line.split())
            str_inventory = items
    return str_inventory

def open_tank(message):
    with open("tank.txt",'w') as tank:
        tank.write(message)

def logit(code,amount,payment):
    with open("log.txt",'a') as file:
        if payment == '1' or payment == '2':
            file.write('{0}, {1}, {2}, {3:.2f}\n'.format(code,gas_name(code),amount[0],amount[1]))

def open_log():
    with open("log.txt","r") as file:
        file.readline()
        lst = file.readlines()
        text = []
        for line in lst:
            text.append(line.split())
    return text
