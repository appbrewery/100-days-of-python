# calculator build in python
# addition

# define the functions
# add function


def add(x, y):
    return x + y


# this function subtract
def subtract(x, y):
    return x - y


# this function multiplies two numbers
def multiply(x, y):
    return x * y


# this function divides two numbers
def divide(x, y):
    return x / y


print("Please select operation \n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

select = float(input("Please select 1 2 3 4 :"))
# define the parameters
number_1 = float(input("Enter your first number"))
number_2 = float(input("Enter your first number"))
# do the calculation
# addition
if select == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))

# subtraction

elif select == 2:
    print(number_1, "+", number_2, "=", subtract(number_1, number_2))

# multiplication

elif select == 3:
    print(number_1, "+", number_2, "=", multiply(number_1, number_2))

# division

elif select == 4:
    print(number_1, "+", number_2, "=", divide(number_1, number_2))
else:
    print("wrong input ")
