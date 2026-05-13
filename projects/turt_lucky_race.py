import turtle
import random

colors = [
    "red", "crimson", "green", "blue", "teal",
    "aquamarine", "pink", "yellow", "cyan", "gold"
]

racers = []

def get_num_of_players():
    players = int(input("How many racers(up to 10) "))
    while players < 1 or players > 10:
        print("Please enter a number from 1 to 10.")
        players = int(input("How many racers(up to 10) "))

    return players

def setup_race(num_players):
    screen = turtle.Screen()
    screen.title("Turtle Race")
    screen.setup(width=700, height=500)

    start_y = -200
    spacing = 400 / (num_players - 1) if num_players > 1 else 0

    for i in range(num_players):
        racer = turtle.Turtle()
        racer.shape("turtle")
        racer.color(colors[i])
        racer.penup()

        y_position = start_y + i * spacing
        racer.goto(-300, y_position)

        racers.append(racer)
    
def draw_finish():
    line = turtle.Turtle()
    line.hideturtle()
    line.speed(0)
    line.penup()
    line.goto(300, -220)
    line.pendown()
    line.pensize(4)
    line.left(90)
    line.forward(440)

# var = some_returning_func()
player_amount = get_num_of_players()
setup_race(player_amount)
draw_finish()

turtle.done()