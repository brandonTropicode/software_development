# - Create a function `def create_user_account()` that takes no parameters and asks the user for 4 things
#     - First name
#     - Last name
#     - Age
#     - Email
# - The function should check if `age` input is an integer, if not ask for it again
# - Return all four data inputs at the end

def create_user_account():
    first = input("your firstname ")
    last = input("your last name ")
    email = input("your email ")
    age = input("your age ")
    mistake_cap = 1
    while not age.isdigit() and mistake_cap > 0:
        #nums only
        mistake_cap -= 1
        print("not number")
        age = input("your age ")
    if mistake_cap == 0:
        print("learn your numbers dummy")
        return
    age = int(age)
    return first,last,email,age
create_user_account()