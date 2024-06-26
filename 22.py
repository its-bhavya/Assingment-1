#python program that returns the minimum and maximum values in a list of numbers
nums = []
length = int(input('Enter the length of list: '))
print("Enter the numbers: ")
for i in range (length):
    num = int(input(">>>"))
    nums.append(num)
min = nums[0]
max = nums[0]
for num in range(length):
    if (nums[num] < min):
        min = nums[num]
    elif (nums[num] > max):
        max = nums[num]
print('Numbers entered: ', nums)
print("Minimum number is: ", min)
print("Maximum number is: ", max)
