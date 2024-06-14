'''program that acts as a simple calculator. It should take two numbers and 
an operator (+, -, *, /) as input and print the result'''
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Enter the operation to performed: ")
oprtr = input("+, -, *, /\n")
if oprtr=='+':
    print("Sum =", num1+num2)
elif oprtr == '-':
    print("Sum =", num1-num2)
elif oprtr == '*':
    print("Product =", num1 * num2)
elif oprtr == '/':
    print("Quotient =", num1/num2)
else:
    print("Please enter an operator from one of the four options above.")