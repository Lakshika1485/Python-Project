print("Welcome!!")

menu = {

    "Chowmin": 80,
    "Kurkure Momos": 70,
    "White Sauce Pasta": 80,
    "Coke": 40,
    "Sandwich": 25,
    "Rajma Rice":60,
    "Chole Rice":60

}

print("Our menu")
print("---------------------------------------------------------")

for item,price in menu.items():
    print(f"{item}: Rs.{price}")

total_order = 0
next_order = True

while next_order:
    order = input("Enter the name of item you want:").title()

    if order in menu:
        total_order += menu[order]
        print(f"{order} added in your order.")
        another_order=input("Do you want to add another item?\n(Yes/No)\n").title()
        print()

        if another_order == "Yes":
            next_order = True
        else:
            next_order = False

    else:
        print(f"Sorry {order} is not available.")
        another_order=input("Do you want to add another item?\n(Yes/No)\n").title()
        print()
        if another_order == 'yes':
            next_order=True
        else:
            next_order = False

print(f"Your total bill is : RS{total_order}")