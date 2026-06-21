from datetime import date

name = input("What is your Name? ")
birth_year_str = input("What is your Year of Birth? ")

try:
	birth_year = int(birth_year_str)
	current_year = date.today().year
	age = current_year - birth_year
	if name:
		print(f"{name}, you are {age} years old.")
	else:
		print(f"You are {age} years old.")
except ValueError:
	print("Please enter a valid year (e.g., 1990).")
	