# program that calculates the factorial of a given number
num = int(input("Enter the number whose factorial to be calculated: "))
fact = 1
if (num < 0):
    print("Please enter a positive integer.")
elif ((num == 0) or (num == 1)):
    print ("Factorial of", num, "= 1")
else:
    for i in range (2, num+1):
        fact *= i
    print("Factorial of", num, "=", fact)