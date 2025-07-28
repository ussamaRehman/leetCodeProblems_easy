from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Problem:
        Given an array of integers nums and an integer k, determine if there are two distinct indices i and j
        in the array such that nums[i] == nums[j] and the absolute difference between i and j is at most k.

        Approach:
        - Use a dictionary to store the most recent index where each number was seen.
        - For each number, check if it has appeared before.
        - If yes, check if the distance between current index and last seen index is <= k.
        - If so, return True.
        - Always update the last seen index of the number in the dictionary.

        Solution:
        - Iterate through nums with index.
        - If the number is found in the dictionary and the distance is within k, return True.
        - Otherwise, update the index in the dictionary.

        Time Complexity: O(n) where n is the length of nums
        Space Complexity: O(n) for the dictionary storing seen elements
        """

        seen = {}  # Dictionary to store the last seen index of each number

        for i in range(len(nums)):
            if nums[i] in seen and i - seen[nums[i]] <= k:
                return True
            # Update the last seen index
            seen[nums[i]] = i

        return False