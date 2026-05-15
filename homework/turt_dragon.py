import turtle

def draw_dragon(order, size, angle):
    """Draws a dragon curve recursively."""
    if order == 0:
        turtle.forward(size)
    else:
        # Recursive steps to build the dragon curve
        draw_dragon(order - 1, size, 90)
        turtle.right(angle)
        draw_dragon_mirror(order - 1, size, 90)

def draw_dragon_mirror(order, size, angle):
    """Mirrored version for recursive folding."""
    if order == 0:
        turtle.forward(size)
    else:
        draw_dragon(order - 1, size, 90)
        turtle.left(angle)
        draw_dragon_mirror(order - 1, size, 90)

# Set up the screen and turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.hideturtle()
t.penup()
t.goto(-100, 0)
t.pendown()

# Draw a dragon curve of order 10
draw_dragon(10, 5, 90)

screen.exitonclick()