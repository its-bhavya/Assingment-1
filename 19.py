#program that removes all punctuation from a given string
punctuation = ['.',',',';',':','!']
str1 = input("Enter string: ")
str1_chars = []
for i in str1:
    if i not in punctuation:
        str1_chars.append(i)
str1 = ''.join(str1_chars)
print(str1)