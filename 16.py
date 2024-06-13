#program in python that counts the frequency of each character in a string
string = input("Enter string: ")
freq = {}
for char in string:
    if char in freq:
        freq[char] +=1
    else:
        freq[char] = 1
print("Frequency of each character.")
for key, value in freq.items():
    print(key ,":", value, end = ', ')
