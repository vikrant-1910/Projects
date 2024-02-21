def main():
    num = float(input("Enter the First NUMBER: "))
    opt = input("Enter OPERATOR (+, -, *, /, %): ")

    if opt in ['+', '-', '*', '/', '%']:
        num1 = float(input("Enter the Second NUMBER: "))

        if opt == '+':
            result = num + num1
        elif opt == '-':
            result = num - num1
        elif opt == '*':
            result = num * num1
        elif opt == '/':
            if num1 != 0:
                result = num / num1
            else:
                print("Cannot divide by zero.")
                return
        elif opt == '%':
            if num1 != 0:
                result = num % num1
            else:
                print("Cannot find the modulus with zero.")
                return

        print(f"Your Answer = {result}")
    else:
        print("OPPS! I CANNOT CALCULATE '__'")

    print("THANK YOU FOR USING MY CALCULATOR")


if __name__ == "__main__":
    print("_____(+,-,/,*,%) WELCOME TO MY CALCULATOR ('>')____")
    main()
