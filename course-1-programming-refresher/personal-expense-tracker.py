import csv
from datetime import datetime

# List to hold expense data
expenses = []
monthly_budget = 0

# Load expenses from file at start
def load_expenses(filename='expenses.csv'):
    global expenses
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            expenses = [row for row in reader]
            for expense in expenses:
                expense['amount'] = float(expense['amount'])
    except FileNotFoundError:
        print("No previous expenses found. Starting fresh.")
    except Exception as e:
        print(f"Error loading expenses: {e}")

# Save expenses to file
def save_expenses(filename='expenses.csv'):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['date', 'category', 'amount', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)
    print("Expenses saved successfully.")

# Add an expense
def add_expense():
    while True:
        date = input("Enter the date (YYYY-MM-DD): ")
        if date.isnumeric():
            date = datetime.strptime(date, '%Y-%m-%d')
            break
        else:
            print("Invalid date. Please enter a valid date in YYYY-MM-DD format.")

    category = input("Enter the category (e.g., Food, Travel): ")
    while True:
        amount = input("Enter the amount spent: ")
        if amount.isnumeric():
            amount = float(amount)
            break
        else:
            print("Invalid amount. Please enter a numeric value.")

    description = input("Enter a brief description of the expense: ")
    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }
    expenses.append(expense)
    print("Expense added successfully.")

# View all expenses
def view_expenses():
    if not expenses:
        print("No expenses to show.")
        return
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. Date: {expense['date']}, Category: {expense['category']}, Amount: ${expense['amount']:.2f}, Description: {expense['description']}")

# Set a monthly budget
def set_budget():
    global monthly_budget
    try:
        monthly_budget = float(input("Enter your monthly budget: "))
        print(f"Monthly budget set to ${monthly_budget:.2f}.")
    except ValueError:
        print("Invalid budget amount. Please enter a numeric value.")

# Track budget
def track_budget():
    total_spent = sum(expense['amount'] for expense in expenses)
    if monthly_budget == 0:
        print("No budget set. Please set a monthly budget first.")
    else:
        remaining_balance = monthly_budget - total_spent
        if remaining_balance < 0:
            print(f"You have exceeded your budget by ${-remaining_balance:.2f}!")
        else:
            print(f"You have ${remaining_balance:.2f} left for the month.")

# Display menu and interact with user
def menu():
    load_expenses()  # Load expenses at the start
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Set and Track Budget")
        print("4. Save Expenses")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            set_budget()
            track_budget()
        elif choice == '4':
            save_expenses()
        elif choice == '5':
            save_expenses()  # Save expenses before exiting
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    menu()
