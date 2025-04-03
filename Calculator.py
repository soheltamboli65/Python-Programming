import tkinter as tk

def calculate(operation):
    num1 = 10
    num2 = 5  # Changed num2 to 5 for division to work

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:

            result = "Cannot divide by zero"
        else:
            result = num1 / num2

    label.config(text=f"Result: {result}")

window = tk.Tk()

add_button = tk.Button(window, text="Add", command=lambda: calculate("add"))
subtract_button = tk.Button(window, text="Subtract", command=lambda: calculate("subtract"))
multiply_button = tk.Button(window, text="Multiply", command=lambda: calculate("multiply"))
divide_button = tk.Button(window, text="Divide", command=lambda: calculate("divide"))
label = tk.Label(window, text="")

add_button.pack()
subtract_button.pack()
multiply_button.pack()
divide_button.pack()
label.pack()

window.mainloop()
