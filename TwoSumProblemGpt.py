from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i in range(size):
            for j in range(i + 1, size):  # clean way to avoid using same index
                if nums[i] + nums[j] == target:
                    return [i, j]

sol = Solution()
nums = [11, 6, 4, 2, 9, 23, 7]
target = 9
answer = sol.twoSum(nums, target)
print(answer)