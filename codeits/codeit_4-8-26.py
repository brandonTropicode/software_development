def kidoradult(age):
    if age < 18:
        print("are you a kid")
    elif age >= 18:
        print("your an adult")
#age_input = int(input("what is your age "))
#kidoradult(age_input)
users = {
    "alex": "supercalifradgilisticespialidocious",
    "mike": "lake awkadegeewabgeeladgeodke"
}
def login(username, password):
    if username in users: #this checks if username(key) is in users(dictionary)
        if password == users[username]:
            print("login successful")
        else:
            print("wrong password buddy")
    else:
        print("wrong username buddy")
User_input = input("what is your user name ")
Pass_input = input("what is your password ")
login(User_input,Pass_input)