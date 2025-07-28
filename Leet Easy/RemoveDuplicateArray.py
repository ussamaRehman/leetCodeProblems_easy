# Problem:
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
# element appears only once. The relative order of the elements should be kept the same. Then return the number of
# unique elements in nums.

# Approach:
# Use two pointers: one slow pointer (i) to track the place of the last unique element,
# and a fast pointer (j) to iterate through the array.
# Whenever a new unique element is found, move it to the correct place in the array using the i pointer.

# Solution:
# Start with i = 0 (first unique element is at index 0).
# Loop through the array from index 1. If nums[j] != nums[i], we’ve found a new unique element.
# Increment i and copy nums[j] to nums[i].
# Return i + 1 as the count of unique elements.

# Time Complexity: O(n) – Each element is visited once.
# Space Complexity: O(1) – No additional space used beyond variables.

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
k = sol.removeDuplicates(nums)   
print("k =", k)     
print("nums =", nums)               
print("nums[:k] =", nums[:k])