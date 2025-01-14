def calculator(operation,a,b):
    if operation == "1":
        return a+b
    elif operation == "2":
        return a-b
    elif operation == "3":
        return a*b
    elif operation == "4":
        if b == 0:
            return "Division by zero is not possible"
        else:
            return a/b
    else:
        return "Invalid choice"
    
print("What do you want to calculate?\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
choice = input("Enter choice: ")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = calculator(choice, a, b)
print("Result: ", result)