while True:
    num1 = float(input("Enter first number: "))
    input_operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if input_operator == "+":
        print(num1 + num2)
    elif input_operator == "-":
        print(num1 - num2)
    elif input_operator == "*":
        print(num1 * num2)
    elif input_operator == "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")

    again = input("Again? (y/n): ")    

    if again == "n":
        break    
    