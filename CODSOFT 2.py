def calculator(x, y, choice):
    x = int(x)
    y = int(y)
    if choice == '1':
        print(x, "+", y, "=", x + y)
    elif choice == '2':
        print(x, "-", y, "=", x - y)
    elif choice == '3':
        print(x, "X", y, "=", x * y)
    elif choice == '4':
        print(x, "/", y, "=", x / y)
    else:
        print("Invalid choice")

# Display the options outside the loop
print("Select operation.")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    # Take input from the user
    choice = input("Enter Your Choice (1 OR 2 OR 3 OR 4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        calculator(num1, num2, choice)
    else:
        print("Invalid Input")
        break
