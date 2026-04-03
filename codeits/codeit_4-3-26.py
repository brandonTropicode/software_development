def which_type_of_day(day):
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    if day in days:    
        if day == "saturday" or day == "sunday":
            print("that is a weekend")
        else:
            print("weekday")
    else:
        print("why u troll :(")
day_input = input("what is your day? ")
which_type_of_day(day_input)

drinks = [
	"Sprite",
	"Coke",
	"Dr.Pepper",
	"Fanta",
    "wAtEr"
]
def vending_machine(choice):
    if choice.isdigit():
        if int(choice) > len(drinks) -1:
            print("error you r a meanie >:(")
            return
        drink = drinks[int(choice)]
        return drink
    else:
        print("error")
        return
drink_input = input("what drink do you want? ")
player_drink = vending_machine(drink_input)
print(player_drink)