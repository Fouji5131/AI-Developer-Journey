name = input("What is your Name? ").strip().title()
# age = input("What is your Age? ").strip().title()
city = input("What is your City? ").strip().title()
job = input("What is your Job? ").strip().title()

while True:
    try:
        age = int(input("What is your Age? "))
        break
    except ValueError:
        print("Please enter a valid age!")

print("\n===== USER PROFILE =====")
print(f"  Name : {name}")
print(f"  Age  : {age}")
print(f"  City : {city}")
print(f"  Job  : {job}")
print("========================")