# 9. Inventory Menu: Create a menu-driven program for a simple shop. The menu should
# allow the user to:
# a. Add an item price to a running total.
# b. Apply a 10% discount to the current total.
# c. View the final total and exit.
# d. Ensure the program loops until the user chooses to exit.

total = 0

while True:
    print("\nMenu")
    print("1. Add Item Price")
    print("2. Apply 10% Discount")
    print("3. View Total and Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        price = float(input("Enter item price: "))
        total += price
        print("Current Total =", total)

    elif choice == "2":
        total = total - (total * 0.10)
        print("Discount Applied")
        print("New Total =", total)

    elif choice == "3":
        print("Final Total =", total)
        print("Exiting Program...")
        break

    else:
        print("Invalid choice")
