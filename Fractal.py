import turtle

def draw_sierpinski_triangle(turtle, order, size):
    if order == 0:
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
    else:
        half_size = size / 2
        draw_sierpinski_triangle(turtle, order - 1, half_size)
        turtle.forward(half_size)
        draw_sierpinski_triangle(turtle, order - 1, half_size)
        turtle.backward(half_size)
        turtle.left(60)
        turtle.forward(half_size)
        turtle.right(60)
        draw_sierpinski_triangle(turtle, order - 1, half_size)
        turtle.left(60)
        turtle.backward(half_size)
        turtle.right(60)

# Initialize turtle
window = turtle.Screen()
window.bgcolor("white")
sierpinski_turtle = turtle.Turtle()
sierpinski_turtle.speed(0)  # Set the fastest drawing speed

# Set initial position and size
sierpinski_turtle.penup()
sierpinski_turtle.goto(-200, -200)
sierpinski_turtle.pendown()

# Draw the Sierpinski Triangle pattern
draw_sierpinski_triangle(sierpinski_turtle, 4, 400)

# Close the turtle graphics window on click
window.exitonclick()
