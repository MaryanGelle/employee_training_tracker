def show_menu():
    """Function to display the menu options."""
    print("Menu")
    print("1. Add training record")
    print("2. View records")
    print("3. Analyse records")
    print("4. Exit")


def choose_menu_option():
    """Function to prompt the user to choose a menu option."""
    choice = input("Choose an option: ")
    # Validate choices for the user
    while choice not in ["1", "2", "3", "4"]:
        print("Invalid option. Please choose a valid menu item.")
        choice = input("Choose an option: ")
    print(f"You selected option {choice}.")
    return choice


def add_training_record():
    """Function to add a training record for an employee."""
    employee_name = input("Enter employee name: ")
    training_name = input("Enter training name: ")

    print("Record added:")
    print(f"Employee: {employee_name}")
    print(f"Training: {training_name}")
    print("")


def view_records():
    """Function to view training records (placeholder)."""
    print("Viewing records feature coming soon!")


def main():
    """Main function to run the Employee Training Tracker app."""
    print("Welcome to Employee Training Tracker")
    print("This app helps track staff training records.")

    print("")

    while True:
        show_menu()

        choice = choose_menu_option()
        if choice == "1":
            add_training_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            print("Analysing records feature coming soon!")
        elif choice == "4":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid menu item.")


if __name__ == "__main__":
    main()
