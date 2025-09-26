# Leaders in the Array 
# Time complexity = O(n^2)

nums = input('Enter the Numbers (,) separated :').split(',')

# Brute force Solution

leaders = []

for i in range(len(nums)-1):
    for j in range(i, len(nums)):
        if nums[i] >= nums[j] and j == len(nums)-1:
            leaders.append(nums[i])
        elif nums[i] >= nums[j]:
            continue
        else:
            break

leaders.append(nums[-1])
print(leaders)


# Optimal Solution

currentLeader = nums[-1]

leaders = []

leaders.append(currentLeader)
for i in range(len(nums)-2, 0, -1):
    if nums[i] > currentLeader:
        currentLeader = nums[i]
        leaders.append(nums[i])

print(leaders)

