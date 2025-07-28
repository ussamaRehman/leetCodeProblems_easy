# Hello, Today it's Saturday 19th July 2025, it's 12:42 am 
# and I am currently solving my first LeetCode problem 
# on road to solving 10,000 LeetCode problems in 3 years.

# The problem I am solving is called a Two Sum Problem.
# We are given an array or list of numbers and a target. 
# We have to find two numbers whose sum equals the target 
# and return the indices of those numbers

# Let's get started
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        answer = None
        for i in range(size-1):
            for j in range(size-1):
                if i == j+1:
                    continue
                if nums[i] + nums[j+1] == target:
                    answer =  [i, j+1]
                    break
            if answer != None:
                return answer
            
sol = Solution()
nums = [11, 6, 4, 2, 9, 23, 7]
target = 9
answer = sol.twoSum(nums, target)
print(answer)