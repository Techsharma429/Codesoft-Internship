def calculator():
    print("----- Simple Calculator -----")
    print("Select Operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", num1 + num2)
            elif choice == '2':
                print("Result:", num1 - num2)
            elif choice == '3':
                print("Result:", num1 * num2)
            elif choice == '4':
                if num2 != 0:
                    print("Result:", num1 / num2)
                else:
                    print("Error: Cannot divide by zero!")
        except ValueError:
            print("Invalid input! Please enter numbers only.")
    else:
        print("Invalid choice! Please select from 1 to 4.")


calculator()