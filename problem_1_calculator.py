from testhelper import test

def calculate(input1, operator, input2):
    if operator == "+":
        return input1 + input2
    elif operator == "-":
        return input1 - input2
    elif operator == "*":
        return input1 * input2
    elif operator == "/":
        if input2 == 0:
            return "Error: Division by zero is not allowed."
        return input1 / input2
    else:
        return "Error: Invalid operator. Please use +, -, *, or /."

try:
    input1 = int(input("Enter the first integer: "))
    operator = input("Enter a mathematical operator (+, -, *, /): ")
    input2 = int(input("Enter the second integer: "))
    
    result = calculate(input1, operator, input2)
    
    print(f"Result: {result}")
except ValueError:
    print("Error: Invalid input. Please enter integers for numbers.")
