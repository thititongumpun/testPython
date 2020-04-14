numsString = '1,5,55,3,90,7,8,2,80'
# numsString = str(input())


# test type
# print(type(numsString))
# split
nums = numsString.split(',')

# convert array to int
for i in range(0, len(nums)):
    nums[i] = int(nums[i])

#sort int numbers
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):

        if nums[i] >= nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

#output
print(nums)

#print(nums[2])




