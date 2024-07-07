import turtle

turtle.forward(100)
turtle.penup() # Lift the pen
turtle.forward(100) # Move forward 100 px without drawing.
turtle.left(90) # Turn left 90 degrees
turtle.pendown() # Lower the pen again.
turtle.forward(100) # Move forward 100 px while drawing

turtle.exitonclick()