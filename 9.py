#program that checks if a substring is present in a given string
string = input("Enter the string: ")
sub_str = input("Enter the substring to  be checked: ")
if sub_str in string:
    print(True)
else:
    print(False)