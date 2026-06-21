email = "test@test.com"
password = "test123"


loginEmail = input("Please enter Email: ")
loginPassword = input("Please enter Password: ")


if (str(loginEmail) == email and str(loginPassword) == password):
    print("Login Succesfull")
else:
    print("Invalid Credentials")