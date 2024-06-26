#program that reads the content of a text file and prints it to the console.
txtfile = open("C:\\Users\\Lenovo\\Assingment-1-1\\txtfile1.txt", 'r')
message = txtfile.read()
print("Contents of the text file:\n", message)