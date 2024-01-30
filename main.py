# pizza order

print("Thank you for ordering Crunch Pizza!")

pizza_size = input("Please select pizza size: S, M, L: ").upper()

if pizza_size == "S":
    bill = 15
elif pizza_size == "M":
    bill = 20
elif pizza_size == "L":
    bill = 25
else:
    print("Invalid size")
    exit()

pepperoni_toppings = input("Would you like to add pepperoni? Y/N ").upper()
extra_cheese = input("Would you like to add extra cheese? Y/N ").upper()

if pepperoni_toppings == "Y":
    if pizza_size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Thank you for choosing Crunch Pizza. Your final bill is: {bill}.")
