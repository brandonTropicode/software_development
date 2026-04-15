# this function gives the amount of access per account type
def access_type(role):
    if role == "admin":
        print("full access")
    elif role == "member":
        print("limited access")
    else:
        print("access denied")
role_input = input("what is your role? ")
access_type(role_input)