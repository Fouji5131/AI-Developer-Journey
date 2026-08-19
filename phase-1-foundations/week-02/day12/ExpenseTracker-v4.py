# ===== EXPENSE TRACKER =====
import csv


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
        return None
    for expense in expenses:
        if expense["title"] == title:
            expenses.remove(expense)
            return expenses
    return None


# 4. Total Spent
def total_spent(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


# 5. Spending by Category
def spending_by_category(expenses, category):
    total = 0
    for expense in expenses:
        if expense["category"] == category:
            total += expense["amount"]
    return category, total


# 6. Generate Report
def generate_report(expenses, *categories):
    if not categories:
        all_cats = set(e["category"] for e in expenses)
        categories = all_cats
    report = {}
    for category in categories:
        total = sum(e["amount"] for e in expenses if e["category"] == category)
        report[category] = total
    return report


# 7. Search Expense
def search_expense(expenses, keyword):
    results = []
    for expense in expenses:
        if keyword.lower() in expense["title"].lower():
            results.append(expense)
    return results


# 8. Sort Expense
def sort_expense(expenses, by="amount"):
    sorted_expenses = sorted(expenses, key=lambda e: e[by])
    return sorted_expenses


# 9. Clear All Expenses
def clear_all_expense(expenses):
    confirm = (
        input("Are you sure? This will delete ALL expenses. (y/n): ").strip().lower()
    )
    if confirm == "y":
        expenses.clear()
        return True
    return False


# 10. Exit
def end_all():
    print("Thank you for using the expense tracker. Goodbye!")


# Display Helper
def display_expenses(expense_list):
    if not expense_list:
        return "No expenses recorded yet."
    lines = [f"{e['title']}: Rs.{e['amount']} ({e['category']})" for e in expense_list]
    return "\n".join(lines)


# Load from CSV
def load_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)
            expenses = []
            for row in reader:
                expenses.append(
                    {
                        "title": row["title"],
                        "amount": int(row["amount"]),
                        "category": row["category"],
                    }
                )
            return expenses
    except FileNotFoundError:
        return []  # first run — no file yet, totally normal
    except PermissionError:
        print("No permission to read this file!")
        return []
    except Exception as e:
        print(f"Unexpected error loading expenses: {e}")
        return []


# Save to CSV
def save_expenses(expenses):
    try:
        with open("expenses.csv", "w", newline="") as file:
            fieldnames = ["title", "amount", "category"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(expenses)
    except PermissionError:
        print("No permission to write this file!")
    except Exception as e:
        print(f"Unexpected error saving expenses: {e}")


def main():
    expenses = load_expenses()  # load on startup

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1.  Add Expense")
        print("2.  View All Expenses")
        print("3.  Delete Expense")
        print("4.  Total Spent")
        print("5.  Spending by Category")
        print("6.  Generate Report")
        print("7.  Search Expense")
        print("8.  Sort Expenses")
        print("9.  Clear All Expenses")
        print("10. Exit")
        print("==========================")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                title = input("Enter the title: ").strip()
                while True:
                    try:
                        amount = int(input("Enter the amount: "))
                        break
                    except ValueError:
                        print("Please enter a valid amount!")
                category = input("Enter the category: ").strip()
                expense = add_expense(expenses, title, amount, category)
                save_expenses(expenses)  # ← save after add
                print(f"✅ '{expense['title']}' added successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            print(display_expenses(view_expenses(expenses)))

        elif choice == "3":
            title = input("Enter the title to delete: ").strip()
            result = delete_expense(expenses, title)
            if result is not None:
                save_expenses(expenses)  # ← save after delete
                print(f"✅ '{title}' deleted successfully.")
            else:
                print("❌ Expense not found.")

        elif choice == "4":
            print(f"💰 Total spent: Rs.{total_spent(expenses)}")

        elif choice == "5":
            category = input("Enter the category: ").strip()
            category, total = spending_by_category(expenses, category)
            print(f"💰 Total spent on {category}: Rs.{total}")

        elif choice == "6":
            if not expenses:
                print("No expenses to report.")
            else:
                report = generate_report(expenses)
                print("\n===== SPENDING REPORT =====")
                for cat, total in report.items():
                    print(f"  {cat}: Rs.{total}")
                print("===========================")

        elif choice == "7":
            keyword = input("Enter the keyword: ").strip()
            result = search_expense(expenses, keyword)
            if result:
                print(f"Found {len(result)} result(s):")
                print(display_expenses(result))
            else:
                print("❌ No expenses found.")

        elif choice == "8":
            print("Sort by: 1. Amount  2. Title")
            sort_choice = input("Choose: ").strip()
            if sort_choice == "1":
                result = sort_expense(expenses, by="amount")
            elif sort_choice == "2":
                result = sort_expense(expenses, by="title")
            else:
                print("Invalid choice.")
                continue
            print(display_expenses(result))

        elif choice == "9":
            cleared = clear_all_expense(expenses)
            if cleared:
                save_expenses(expenses)  # ← save after clear
                print("✅ All expenses cleared.")
            else:
                print("Cancelled.")

        elif choice == "10":
            end_all()
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
