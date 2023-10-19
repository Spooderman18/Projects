
def add(num1, num2):  #to add two numbers
    return num1 + num2

def subtract(num1, num2): #to subtract two numbers
    return num1 - num2

def multiply(num1, num2): #to multiply two numbers
    return num1 * num2

def divide(num1, num2):#to divide two numbers
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

while True:
    print("Please select operation -\n" \
          "1. Add\n" \
          "2. Subtract\n" \
          "3. Multiply\n" \
          "4. Divide\n" \
          "5. Exit\n")

    # Taking input from the user
    select = int(input("Select operations from 1, 2, 3, 4, 5: "))

    if select == 5:
        break  # to exit the loop and end the program

    number_1 = float(input("Enter the first number: "))
    number_2 = float(input("Enter the second number: "))

    if select == 1:
        print(number_1, "+", number_2, "=", add(number_1, number_2))
    elif select == 2:
        print(number_1, "-", number_2, "=", subtract(number_1, number_2))
    elif select == 3:
        print(number_1, "*", number_2, "=", multiply(number_1, number_2))
    elif select == 4:
        result = divide(number_1, number_2)
        if isinstance(result, str):
            print(result)
        else:
            print(number_1, "/", number_2, "=", result)
    else:
        print("Invalid input. Please try again.")

