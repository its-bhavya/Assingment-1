#program that counts the occurrences of a specific element in a list
n = int(input("Enter the length of list: "))
L = []
for i in range (n):
    element = input(">>>")
    L.append(element)
x = input("Enter the element to be checked: ")
count = 0
for i in L:
    if(i ==x):
        count +=1
print("Count =", count)