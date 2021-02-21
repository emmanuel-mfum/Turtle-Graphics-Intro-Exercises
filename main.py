import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)

timmy.shape("turtle")
timmy.color("blue")

# Drawing a square

# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# Making a dashed line

# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()  # puts the pen up, no drawing while moving
#     timmy.forward(10)
#     timmy.pendown()  # puts the pen down, drawing while moving


# Making a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

# is_Done = False
# colors = ["red", "blue", "gold", "green", "firebrick", "cyan", "purple", "black"]
# sides = 3
# angle = 360/sides
#
#
# while not is_Done:
#     for n in range(sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#     sides += 1
#     angle = 360 / sides
#     timmy.color(random.choice(colors))
#
#     if sides > 10:
#         break


# Making a random walk

# timmy.pensize(15)
# timmy.speed("fastest")
# directions = [0, 90, 180, 270]
#
#

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#
#     hue = (r, g, b)
#     return hue
#
#
# def random_path(color_passed, direction_passed):
#     timmy.color(color_passed)
#     timmy.setheading(direction_passed)
#     timmy.forward(30)
#
#
# for n in range(200):
#     color = random_color()
#     direction = random.choice(directions)
#     random_path(color, direction)


# Making a spirograph
#
# angle = 0
# timmy.speed("fastest")
#
#
# def make_spirograph(size_of_gap):
#     for n in range(int(360/size_of_gap)):
#         timmy.color(random_color())
#         timmy.circle(100)
#         current_heading = timmy.heading()
#         timmy.setheading(current_heading + size_of_gap)
#
#
# make_spirograph(5)



screen = t.Screen()  # makes the screen appears

screen.exitonclick()  # the screen will exit upon click
