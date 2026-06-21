# LISTS
expenses = ["rent", "food", "transport", "utilities"]

# Indexing
print(expenses[0])      # "rent"
print(expenses[-1])     # "utilities" (last item)

# Slicing
print(expenses[1:3])    # ["food", "transport"]

# Modifying
expenses.append("internet")       # add to end
expenses.insert(1, "groceries")   # add at position
expenses.remove("food")           # remove by value
expenses.pop()                    # remove last item
expenses.pop(0)                   # remove by index

# Useful operations
print(len(expenses))              # count items
print("rent" in expenses)         # True/False check
expenses.sort()                   # sort alphabetically

# Looping
for expense in expenses:
    print(expense)




# TUPLES
coordinates = (40.7128, -74.0060)   # latitude, longitude
rgb = (255, 128, 0)                  # color values

print(coordinates[0])    # 40.7128
# coordinates[0] = 999  # ❌ TypeError — tuples cannot be modified




# DICTIONARIES
expense = {
    "title": "Grocery Shopping",
    "amount": 2500,
    "category": "Food",
    "date": "2024-01-15"
}

# Access
print(expense["title"])              # "Grocery Shopping"
print(expense.get("amount"))         # 2500
print(expense.get("tax", 0))         # 0 — default if key missing

# Modify
expense["amount"] = 3000             # update existing
expense["currency"] = "PKR"          # add new key

# Remove
del expense["date"]
expense.pop("currency")

# Check key exists
print("title" in expense)            # True

# Loop through
for key, value in expense.items():
    print(f"{key}: {value}")

# All keys / all values
print(expense.keys())
print(expense.values())




# LIST of DICTIONARIES
expenses = [
    {"title": "Rent",      "amount": 25000, "category": "Housing"},
    {"title": "Groceries", "amount": 8000,  "category": "Food"},
    {"title": "Netflix",   "amount": 1500,  "category": "Entertainment"},
    {"title": "Petrol",    "amount": 3000,  "category": "Transport"},
]

# Loop and display
for expense in expenses:
    print(f"{expense['title']}: Rs.{expense['amount']}")

# Filter by category
food = [e for e in expenses if e["category"] == "Food"]

# Total amount
total = sum(e["amount"] for e in expenses)
print(f"Total: Rs.{total}")