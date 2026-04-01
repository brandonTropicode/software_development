drinks = [
	"Sprite",
	"Coke",
	"Dr.Pepper",
	"Fanta",
    "wAtEr"
]
def vending_machine(choice):
    drink = drinks[choice]
    return drink
#print(f'thank you for your purchase of {vending_machine(4)} it costs $500000000000000000000')
daily_weather = {
	"monday":67,
	"tuesday": 67,
	"wednesday": 67,
	"thursday":92,
	"friday": 96,
	"saturday": 49,
	"sunday": 55}
def weather_by_day():
    for i in daily_weather:
        print(f"{daily_weather[i]}")
#weather_by_day()

# 2! = 1*2
# 3! = 1*2*3
# 4! = 1*2*3*4

def factorial(x):
    if x==0:
        return 1
    return x * factorial(x-1)
print(factorial(774))


# Create function get_vehicle_type(num_wheels) that returns one of these 'bike', 'car', 'bus' based on the number of wheels given by num_wheels

def get_vehicle_type(num_wheels):
    if num_wheels==2:
        print("that is one cool bike")
    elif num_wheels== 4:
        print("nice car dude")
    elif num_wheels > 4:
        print("nice bus")
    else:
        print("quit trolling goofy lookin troll")
get_vehicle_type(4)