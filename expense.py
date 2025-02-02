expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    expenses.append({"name": name, "amount": amount, "category": category})
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    total = 0
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['name']} - Rs.{expense['amount']} ({expense['category']})")
        total += expense["amount"]
    print(f"Total Expenses: Rs.{total}")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
