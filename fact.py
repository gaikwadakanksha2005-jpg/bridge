import math

while True:
    ch = input("Enter choice (+, -, *, /, ! or exit): ")

    if ch == "exit":
        print("Calculator terminated")
        break

    if ch == "!":
        n = int(input("Enter number: "))
        print("Factorial =", math.factorial(n))

    else:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if ch == "+":
            print("Result =", a + b)
        elif ch == "-":
            print("Result =", a - b)
        elif ch == "*":
            print("Result =", a * b)
        elif ch == "/":
            print("Result =", a / b)
        else:
            print("Invalid choice")