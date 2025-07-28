# Problem: Majority Element
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.
#
# Approach:
# - Boyer-Moore Voting Algorithm.
# - Maintain a candidate and a counter.
# - Iterate through the array, adjusting the candidate and counter.
# - Guaranteed to return the majority element since it always exists.
#
# Time Complexity: O(n) - Single pass through the array.
# Space Complexity: O(1) - Constant space.

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Finds the majority element in the array using Boyer-Moore Voting Algorithm.
        :param nums: List[int] - input array of integers
        :return: int - the majority element
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

# Test case
if __name__ == "__main__":
    sol = Solution()
    nums = [2, 2, 1, 1, 1, 2, 2]
    print("Majority element:", sol.majorityElement(nums))  # Output: 2


