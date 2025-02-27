import math

# Factorial Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Area of Circle Function
def area_of_circle(radius):
    return math.pi * radius ** 2

# Area of Triangle Function
def area_of_triangle(base, height):
    return 0.5 * base * height

# Area of Rectangle Function
def area_of_rectangle(length, width):
    return length * width

# Area of Square Function
def area_of_square(side):
    return side ** 2

# Basic Calculator Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    else:
        return a / b

# Calculator Function
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print(f"The result is {add(num1, num2)}")
    elif choice == '2':
        print(f"The result is {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result is {multiply(num1, num2)}")
    elif choice == '4':
        print(f"The result is {divide(num1, num2)}")
    else:
        print("Invalid input")

# Main Function
def main():
    print("Choose an option:")
    print("1. Factorial")
    print("2. Area of Circle")
    print("3. Area of Triangle")
    print("4. Area of Rectangle")
    print("5. Area of Square")
    print("6. Calculator")
    
    option = input("Enter your choice: ")
    
    if option == '1':
        num = int(input("Enter a number for factorial: "))
        print(f"Factorial: {factorial(num)}")
    
    elif option == '2':
        radius = float(input("Enter radius of the circle: "))
        print(f"Area of circle: {area_of_circle(radius)}")
    
    elif option == '3':
        base = float(input("Enter base of the triangle: "))
        height = float(input("Enter height of the triangle: "))
        print(f"Area of triangle: {area_of_triangle(base, height)}")
    
    elif option == '4':
        length = float(input("Enter length of the rectangle: "))
        width = float(input("Enter width of the rectangle: "))
        print(f"Area of rectangle: {area_of_rectangle(length, width)}")
    
    elif option == '5':
        side = float(input("Enter side length of the square: "))
        print(f"Area of square: {area_of_square(side)}")
    
    elif option == '6':
        calculator()
    
    else:
        print("Invalid option!")

# Example Usage
main()
