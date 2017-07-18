from turtle import *
import math
import turtle, random

# Name your Turtle.
frankie = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
frankie.setposition(x_pos, y_pos)
size=100

### Write your code below:

pendown()
colors  = ["red","green","blue","orange","purple","pink","yellow"] # Make a list of colors to picvk from

# draws a square
#for num in range(4):
    #forward(100)
    #left(90)

penup()
#forward(50)
pendown()


#draws a triangle
def drawTriangle():
    begin_fill()
    for num in range(3):
        forward(size)
        left(120)
    end_fill()

def foundation():
    for num in range(12):
        color = random.choice(colors) #Choose a random color
        fillcolor(color)
        drawTriangle()
        right(30)

for num in range(20):
    foundation()
    size-=20



# Close window on click.
exitonclick()
