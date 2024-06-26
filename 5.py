#program that takes a string input from the user and writes it to a text file
txtfile = open("C:\\Users\\Lenovo\\Assingment-1-1\\txtfile1.txt", 'w')
message = input("Please enter your message: ")
txtfile.write(message)
