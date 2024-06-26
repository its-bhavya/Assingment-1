#python program that checks if two strings are anagrams of each other.
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1_chars = list(str1.lower())
str2_chars = list(str2.lower())

str1_chars.sort()
str2_chars.sort()

if str1_chars == str2_chars:
    print("They are anagrams")
else:
    print("They aren't anagrams.")

    


        