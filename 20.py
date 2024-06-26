#program that takes a list of numbers and returns their sum.
n = int(input("Length of list: "))
nums = []
for i in range(1, n+1):
    num = int(input("Enter number: "))
    nums.append(num)
sum = 0
for i in range(len(nums)):
    sum += nums[i]
print("Sum  =", sum)