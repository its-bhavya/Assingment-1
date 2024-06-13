#program that calculates the sum of the digits of a given number.
number = int(input("Enter the number: "))
sum = 0
num = number
while num > 0:
    dig = num % 10
    sum += dig
    num //= 10
print("Sum of the digits of", number, '=', sum)