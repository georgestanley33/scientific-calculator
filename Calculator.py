import math

while True:
    print("")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Exponentiation")     # Lists all the functions
    print("6: Square Root")
    print("7: Logarithm")
    print("8: Trigonometry")
    print("")

    choice = int(input("Which function would you like to carry out? (Enter the number before it): "))
    print("")

    if choice == 1:
        print("Addition")
        print("")
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))      # Addition
        answer = num1+num2
        print("")
        print(f"{num1} + {num2} = {answer}")
        print("")

    if choice == 2:
        print("Subtraction")
        print("")
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        print("")                                       # Subtraction
        answer = num1 - num2
        print(f"{num1} - {num2} = {answer}")
        print("")

    if choice == 3:
        print("Multiplication")
        print("")
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        answer = num1 * num2                            # Multiplication
        print("")
        print(f"{num1} * {num2} = {answer}")
        print("")

    if choice == 4:
        print("Division")
        print("")
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))       # Division
        print("")
        if num2 == 0:
                print("Error, you cannot divide by 0")  # Provides an error if trying to divide by 0 (not possible)
                break
        else:
            answer = num1 / num2
            print(f"{num1} / {num2} = {answer}")
            print("")

    if choice == 5:
        print("Exponential")
        print("")
        num1 = int(input("Enter the base number: "))
        num2 = int(input("Enter the exponent: "))
        answer = num1 ** num2
        print("")                                           # Exponentials
        print("")
        print(f"{num1} ^ {num2} = {answer}")
        print("")

    if choice == 6:
        print("Square Root")
        print("")
        num1 = int(input("Enter the number you want to square root: "))
        print("")
        answer = math.sqrt(num1)
        print(f"Square root of {num1} = {answer}")                              # Square Root
        print("")

    if choice == 7:
        print("1: Base 10")
        print("2: Natural log")
        print("")
        logType = int(input("Which type of logarithm do you want ot perform? (enter the number): "))
        print("")

        if logType == 1:
            print("Base 10")
            print("")
            num1 = int(input("Enter the number you want to perform log base 10 on: "))
            print("")                                                                       #base 10 log
            answer = math.log10(num1)
            print(f"log10({num1}) = {answer}")
            print("")

        if logType == 2:
            print("Natural log")
            print("")
            num1 = int(input("Enter the number you want the natural log of: "))
            answer = math.log(num1)                                                     #natural log
            print(f"Natural log of {num1} = {answer}")
            print("")

    if choice == 8:
        print("1: Sin")
        print("2: Cos")
        print("3: Tan")
        print("")               #trigonometry menu
        trigType = int(input("Which type of trigonometry do you want? (Enter the number): "))
        print("")

        if trigType == 1:
            num1 = int(input("Enter the number you want the sine of (in radians): "))
            print("")
            answer = math.sin(num1)
            print(f"sin({num1}) = {answer}")        #sin
            print("")

        if trigType == 2:
            num1 = int(input("Enter the number you want the cosine of (in radians): "))
            print("")
            answer = math.cos(num1)
            print(f"cos({num1}) = {answer}")        #cos
            print("")

        if trigType == 3:
            num1 = int(input("Enter the number you want the tangent of (in radians): "))
            print("")
            answer = math.tan(num1)
            print(f"tan({num1}) = {answer}")        #tan
            print("")

    carryon = input("Do you want to perform another calculation? (Y/N) : ")
    if carryon.lower() == "n":
        break