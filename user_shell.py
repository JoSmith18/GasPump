from gascore import *
from disk import *

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

payment = valid_pay()

selection = """ Select Code Of Gas Type:
    \t1. Regular: 2.08
    \t2. Midgrade: 2.23
    \t3. Premium: 2.36
  """
code = input(selection)

amount = addup(payment,code)

logit(code,amount,payment)

inventory = load_inventory()

message = write_message(inventory,code,amount)

open_tank(message)
