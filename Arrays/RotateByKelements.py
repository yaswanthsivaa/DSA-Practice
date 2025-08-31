# Rotate Array By K elements

nums = [1,2,3,4,5]

shift = int(input('Enter the Element :'))

for i in range(1,len(nums)):

    if i <= shift:
        nums.append(i)
    
del nums[0:shift]

print(nums)

