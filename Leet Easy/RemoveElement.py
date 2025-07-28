# Problem:
# Given an integer array nums and an integer val, remove all occurrences of val in-place.
# Return the number of elements remaining after removing val.
# The remaining elements can be in any order, and content beyond the returned length is ignored.

# Approach:
# Use the two-pointer technique.
# - One pointer (read) goes through all elements.
# - Another pointer (write) tracks the position to overwrite.
# - If nums[read] != val, assign nums[write] = nums[read] and increment write.

# Solution:
# In-place overwrite using two pointers.
# Time Complexity: O(n)
# Space Complexity: O(1)
from typing import List
class Solution:
    def removeElement(self, nums: List, val: int) -> int:
        write = 0
        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
        return write

nums = [0, 1, 2, 2, 3, 0, 4, 2]
sol = Solution()
k = sol.removeElement(nums, val = 2)
# Sorting the valid part to match expected output format (optional)
nums[:k] = sorted(nums[:k])
print(nums)
print(k)