# ===== EXPENSE TRACKER =====
expenses = []

# 1. Add Expense
def add_expense():
    title = input("Enter the title: ").strip()

    while True:
        try:
            amount = int(input("Enter the amount: "))
            break
        except ValueError:
            print("Please enter a valid amount!")

    category = input("Enter the category: ")

    expense = {
        "title": title,
        "amount": int(amount),
        "category": category
    }
   
    expenses.append(expense)
    # print(f"Expense '{expense}' added successfully.")
    return expense

# 2. View All Expenses
def view_expenses():
    # for expense in expenses:
        # print(f"Title: {expense['title']}, Amount: {expense['amount']}, Category: {expense['category']}")
        # return expenses
    return expenses

# 3. Delete Expense
def delete_expense():
    if not expenses:
        return None   # nothing to delete
        
    title = input("Enter the title of the expense to delete: ")
    for expense in expenses:
        if expense['title'] == title:
            expenses.remove(expense)
            return expenses
            # print(f"Expense '{title}' deleted successfully.")
            # break

# 4. Total Spent
def total_spent():
    total = 0
    for expense in expenses:
        total += expense['amount']
    # print(f"Total spent: {total}")
    return total

# 5. Spending by Category
def spending_by_category():
    category = input("Enter the category: ")
    total = 0
    for expense in expenses:
        if expense['category'] == category:
            total += expense['amount']
    # print(f"Total spent on {category}: {total}")
    return category, total

# 6. Exit
def end_all():
    print("Thank you for using the expense tracker. Goodbye!")
    
def display_expenses(expense_list):
    if not expense_list:
        return "No expenses recorded yet."
    lines = [f"{e['title']}: Rs.{e['amount']} ({e['category']})" for e in expense_list]
    return "\n".join(lines)

def main():
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
        if choice == '1':
            try:
                expense = add_expense()
                if expense is not None:
                    print(f"Expense '{expense}' added successfully.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '2':
            print(display_expenses(view_expenses()))
        elif choice == '3':
            result = delete_expense()
            if result is not None:
                print(f"Expense '{result}' deleted successfully.")
            else:
                print("Expense not found.")
        elif choice == '4':
            print(f"Total spent: {total_spent()}")
        elif choice == '5':
            category, total = spending_by_category()
            print(f"Total spent on {category}: {total}")
        elif choice == '6':
            end_all()
            break
        else:
            print("Invalid choice. Please try again.")

    
if __name__ == "__main__":
    main()