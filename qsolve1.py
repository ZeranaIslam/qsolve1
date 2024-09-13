1.Create a simple calculator that performs basic arithmetic operation(addition,subtraction,multiplication,division)
  based on user input.


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

print("Please select operation -\n" \
        "1. Addition\n" \
        "2. Subtraction\n" \
        "3. Multiplication\n" \
        "4. Division\n")
		

select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=",
                    addition(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtraction(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiplication(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=",
                    division(number_1, number_2))
else:
    print("Invalid input")
