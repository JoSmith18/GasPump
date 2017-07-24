from gascore import valid_pay, gas_name,logit,load_inventory,close_inventory, refill, revenue, menu, add_payafter, add_prepay, addup

payment = valid_pay()

selection = """ Select Code Of Gas Type:
    \t1. Regular: 2.02
    \t2. Midgrade: 2.14
    \t3. Premium: 2.27
  """
code = input(selection)

amount = addup(payment,code)

logit(code,amount,payment)

inventory = load_inventory()

close_inventory(inventory,code,amount)