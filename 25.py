#program that copies the contents of one text file to another
file1 = open("txtfile1.txt", "r")
file2 = open("txtfile2.txt", "w")
content = file1.readlines()
file2.writelines(content)
print("File content copied!")