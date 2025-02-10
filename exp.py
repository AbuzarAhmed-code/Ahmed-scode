from datetime import datetime

# Welcome message
print("WELCOME TO EXPENSE & INVESTMENT TRACKER!")
a = input("enter your name:  ")
b = input("enter your age:  ")

# Storage for expenses and investments
expenses = []  
investments = []

def get_time():
    """Returns current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def add_expense():
    """Adds an expense with date & time."""
    amount = input("Enter expense amount: ₹")
    reason = input("Enter reason for expense: ")
    expenses.append((get_time(), reason, amount))
    print(f"Expense Added: ₹{amount} for {reason}\n")

def show_expenses():
    """Displays all recorded expenses."""
    if not expenses:
        print("No expenses recorded yet!\n")
    else:
        print("\n Expense History:")
        for time, reason, amount in expenses:
            print(f"{time} → {reason}: ₹{amount}")
        print()

def add_investment():
    """Adds an investment with date & time."""
    amount = input("Enter investment amount: ₹")
    reason = input("Enter the stock name in which you have invested: ")
    investments.append((get_time(), reason, amount))
    print(f"Investment Added: ₹{amount} for {reason}\n")

def show_investments():
    """Displays all recorded investments."""
    if not investments:
        print("No investments recorded yet!\n")
    else:
        print("\n Investment History:")
        for time, reason, amount in investments:
            print(f"{time} → {reason}: ₹{amount}")
        print()

# Main menu loop
while True:
    print("\nChoose an option:")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Add Investment")
    print("4. Show Investments")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        add_investment()
    elif choice == "4":
        show_investments()
    elif choice == "5":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice! Please enter 1-5.\n")