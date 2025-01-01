import turtle

def turtle_run():
    wn = turtle.Screen()      # creates a graphics window
    wn.bgcolor("lightgreen")
    
    alex = turtle.Turtle()    # create a turtle named alex
    alex.pensize(5)
    
    alex.forward(150)         # tell alex to move forward by 150 units
    alex.left(90)             # turn by 90 degrees
    alex.forward(75)          # complete the second side of a rectangle
    alex.left(100)
    alex.forward(75)
    alex.right(20)
    alex.forward(80)

    wn.exitonclick()

turtle_run()
turtle.done()
