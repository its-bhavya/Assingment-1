#python program that checks if two strings are anagrams of each other.
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
str1_chars = []
str2_chars = []
for i in str1:
    str1_chars.append(i)
for i in str2:
    str2_chars.append(i)
str1_chars.sort()
str2_chars.sort()
if str1_chars == str2_chars:
    print("They are anagrams")
else:
    print("they aren't anagrams.")

    


        