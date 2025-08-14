nums = [-1,0]
target = -1
complements = {}

for i in range(len(nums)):
    complement = target - nums[i]

    if complement not in complements:
        complements[complement] = i
    
    if nums[i] in complements:
        print(complements[nums[i]]+1, i+1)

