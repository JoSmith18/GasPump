from gascore import *
from datetime import *
from disk import *

inventory = load_inventory()

name = input("Hi What Is Your Name\n")

print('Hello {} You Have Clearance\n'.format(name))

decision = """ Admin Decisions
\t1. Refill The Tanks
\t2. Check The Revenue
\t3. Open Log
\t4. Look At Tanks
"""

choice = input(decision)

if choice.strip() == '1'.strip():
    message = refill(inventory)
    open_tank(message)
    with open("tank.txt", "r") as tank:
        print(tank.read())

elif choice.strip() == '2'.strip():
    text = open_log()
    print(revenue(text))

elif choice.strip() == '3'.strip():
    with open("log.txt", "r") as file:
        print(file.read())

elif choice.strip() == '4'.strip():
    with open("tank.txt","r") as tanks:
        print(tanks.read())
        
else:
    print("Error we are starting over")

with open("adminlog.txt","a") as log:
    log.write("{},{}, {}\n".format(name, choices(choice), datetime.today()))
