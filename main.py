import turtle

# Draw the interface
turtle.title("Calculator By ShubboXD")
turtle.setup(width=500, height=500)
turtle.penup()
turtle.goto(-100, 150)
turtle.pendown()
turtle.write("Welcome to Calculator", font=("Arial", 20, "bold"))
turtle.penup()
turtle.goto(-50, 100)
turtle.pendown()
turtle.write("Enter first number: ", font=("Arial", 14, "normal"))
turtle.penup()
turtle.goto(-50, 50)
turtle.pendown()
turtle.write("Enter second number: ", font=("Arial", 14, "normal"))
turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()
turtle.write("Enter operator (+, -, *, /): ", font=("Arial", 14, "normal"))
turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()
turtle.write("Result: ", font=("Arial", 14, "normal"))

# Get inputs from user
num1 = float(turtle.textinput("First number", "Enter first number:"))
num2 = float(turtle.textinput("Second number", "Enter second number:"))
operator = turtle.textinput("Operator", "Enter operator (+, -, *, /):")

# Calculate result
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    turtle.write("Invalid operator", font=("Arial", 14, "normal"))

# Show result
turtle.penup()
turtle.goto(50, -50)
turtle.pendown()
turtle.write(result, font=("Arial", 14, "normal"))

turtle.done()
