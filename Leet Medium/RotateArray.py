nums = [1,2,3,4]

k = 1
temp = None
for i in range(k):
    temp = len(nums) - 1
    for j in range(len(nums) - 1, 0, -1):
        nums.insert(j, nums[j-1])
        nums.pop()
    nums[0] = temp
    

print(nums)