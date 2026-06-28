import gspread
import datetime
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("employee_training_tracker")

training_records_worksheet = SHEET.worksheet("training_records")

training_records = training_records_worksheet.get_all_records()


def show_menu():
    """Function to display the menu options."""
    print("Menu")
    print("1. Add training record")
    print("2. View records")
    print("3. Search records")
    print("4. Analyse records")
    print("5. Delete records")
    print("6. Exit")


def choose_menu_option():
    """Function to prompt the user to choose a menu option."""
    choice = input("Choose an option: ")
    # Validate choices for the user
    while choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid option. Please choose a valid menu item.")
        choice = input("Choose an option: ")

    return choice


def add_training_record():
    """Function to add a training record for an employee."""
    employee_name = input("Enter employee name: ").strip()
    training_name = input("Enter training name: ").strip()
    status = input(
        "Enter training status (Completed/In progress/Not started): ").strip()

    # Get current date and time
    record_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save to Google Sheet
    new_record = [employee_name, training_name, status, record_date]
    training_records_worksheet.append_row(new_record)

    # Update the Python list
    recorded = {
        "employee_name": employee_name,
        "training_name": training_name,
        "status": status,
        "record_date": record_date
    }

    training_records.append(recorded)

    print("Record added.")
    print(f"Employee: {employee_name}")
    print(f"Training: {training_name}")
    print(f"Status: {status}")
    print(f"Record Date: {record_date}")
    print("")


def view_records():
    """Function to view all training records."""
    if not training_records:
        print("No records found.")
        return

    print("\nTraining Records:")
    for index, record in enumerate(training_records, start=1):
        print(
            f"{index}. Employee: {record['employee_name']}, Training: {record['training_name']}, Status: {record['status']}, Record Date: {record['record_date']}")


def search_records():
    """Function to search training records."""
    search_name = input("Enter name to search for: ").strip()
    found = False

    for record in training_records:
        if record['employee_name'].lower() == search_name.lower():
            print(f"\nRecord found for employee: {record['employee_name']}")
            print(f"Training: {record['training_name']}")
            print(f"Status: {record['status']}")
            print(f"Record Date: {record['record_date']}")
            found = True
    if not found:
        print("No record found.")


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
            search_records()
        elif choice == "4":
            print("Analysing records feature coming soon!")
        elif choice == "5":
            print("Deleting records feature coming soon!")
        elif choice == "6":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid menu item.")


if __name__ == "__main__":
    main()
