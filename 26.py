'''program in python that checks if a string starts with a given prefix
or ends with a given suffix.'''
#there also exist pre-defined functions 'startswith and 'endswith' to check for prefix and suffix
string = input("Enter string: ")
length = len(string)
choice = input("Type 'P' for Prefix, or 'S' for Suffix: ")
start = 0
end = 0
if choice.lower() == 'p':
    prefix = input("Enter the prefix: ")
    n = len(prefix)
    if n > length:
        print("No")
    for i in range(n):
        if string[i] != prefix[i]:
            print("No")
            break
    print("Yes")
    
elif choice.lower() == 's':
    suffix = input("Enter the suffix: ")
    n = len(suffix)
    if n > length:
        print("No")
    for i in range(1, n+1):
        if suffix[-i]!= string[-i]:
            print("No")
            break
    print("Yes")
else:
    print("Please choose from S or P.")