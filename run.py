print("Welcome to Employee Training Tracker")
print("This app helps track staff training records.")

print("")
print("Menu")
print("1. Add training record")
print("2. View records")
print("3. Analyse records")
print("4. Exit")

choice = input("Choose an option: ")

print(f"You selected option {choice}.")

if choice == "1":
    employee_name = input("Enter employee name: ")
    training_name = input("Enter training name: ")

    print("Record added:")
    print(f"Employee: {employee_name}")
    print(f"Training: {training_name}")
elif choice == "2":
    print("Viewing records feature coming soon!")
elif choice == "3":
    print("Analysing records feature coming soon!")
elif choice == "4":
    print("Exiting the app. Goodbye!")
else:
    print("Invalid option. Please choose a valid menu item.")
