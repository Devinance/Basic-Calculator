def calculator():
    while True:
        print("Welcome to the calculator!")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 5:
            break
        elif choice in [1,2,3,4]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == 1:
                result = num1 + num2
                print("Result: ", result)
            elif choice == 2:
                result = num1 - num2
                print("Result: ", result)
            elif choice == 3:
                result = num1 * num2
                print("Result: ", result)
            elif choice == 4:
                result = num1 / num2
                print("Result: ", result)
        else:
            print("Invalid input. Try again.")

calculator()