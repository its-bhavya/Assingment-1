#program that converts temperature from Celsius to Fahrenheit and vice versa based on user input
print("How would you like to convert the temperature? ")
print("FC: Fahrenheit to Celsius")
print("CF: Celsius to Fahrenheit")
choice = input(">>>")
if choice.lower() == 'fc':
    temp = float(input("Enter temperature in Fahrenheits: "))
    cels_temp = ((temp-32)*5)/9
    print("The temperature =", cels_temp, "°C")
elif choice.lower() == "cf":
    temp = float(input("Enter temperature in Celsius: "))
    fahr_temp = ((temp*9)/5) + 32
    print("The temperature =", fahr_temp, "°F") 
else:
    print("Please choose from among FC or CF only.")