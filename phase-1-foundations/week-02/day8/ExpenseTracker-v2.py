# ===== EXPENSE TRACKER =====

# 1. Add Expense
def add_expense(expenses, title, amount, category="General"):
    if amount <= 0:
        raise ValueError("Amount must be positive")

    expense = {"title": title, "amount": int(amount), "category": category}

    expenses.append(expense)
    return expense


# 2. View All Expenses
def view_expenses(expenses):
    return expenses

# 3. Delete Expense
def delete_expense(expenses, title):
    if not expenses:
        return None  # nothing to delete

    # title = input("Enter the title of the expense to delete: ")
    for expense in expenses:
        if expense["title"] == title:
            expenses.remove(expense)
            return expenses

# 4. Total Spent
def total_spent(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total

# 5. Spending by Category
def spending_by_category(expenses):
    category = input("Enter the category: ")
    total = 0
    for expense in expenses:
        if expense["category"] == category:
            total += expense["amount"]
    return category, total

# 6. Report
def generate_report(expenses, *categories):
    if not categories:
        # show all categories
        all_cats = set(e["category"] for e in expenses)
        categories = all_cats

    report = {}
    for category in categories:
        total = sum(e["amount"] for e in expenses if e["category"] == category)
        report[category] = total
    return report


# 7. Exit
def end_all():
    print("Thank you for using the expense tracker. Goodbye!")

def display_expenses(expense_list):
    if not expense_list:
        return "No expenses recorded yet."
    lines = [f"{e['title']}: Rs.{e['amount']} ({e['category']})" for e in expense_list]
    return "\n".join(lines)

def main():
    expenses = []

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Delete Expense")
        print("4. Total Spent")
        print("5. Spending by Category")
        print("6. Exit")
        print("==========================")
        choice = input("Enter your choice: ")
        if choice == "1":
            try:
                title = input("Enter the title: ").strip()

                while True:
                    try:
                        amount = int(input("Enter the amount: "))
                        break
                    except ValueError:
                        print("Please enter a valid amount!")

                category = input("Enter the category: ")

                expense = add_expense(expenses, title, amount, category)
                if expense is not None:
                    print(f"Expense '{expense}' added successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            print(display_expenses(view_expenses(expenses)))

        elif choice == "3":
            try:
                title = input("Enter the title: ").strip()
                result = delete_expense(expenses, title)
                if result is not None:
                    print(f"Expense '{result}' deleted successfully.")
                else:
                    print("Expense not found.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            print(f"Total spent: {total_spent(expenses)}")

        elif choice == "5":
            category, total = spending_by_category(expenses)
            print(f"Total spent on {category}: {total}")

        elif choice == "6":
            report = generate_report(expenses)
            print(f"{report}")

        elif choice == "7":
            end_all()
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
