from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Problem:
        Given an array nums where each element represents the max jump length 
        from that position, determine if you can reach the last index.

        Approach:
        - Use a greedy strategy to keep track of the farthest index reachable at any point.
        - Iterate through nums:
            - If the current index > max_reach → stuck → return False.
            - Update max_reach = max(max_reach, i + nums[i]).
        - If max_reach >= last index → return True.

        Complexity:
        - Time: O(n) — single pass through nums.
        - Space: O(1) — constant extra space.
        """
        max_reach = 0
        last_index = len(nums) - 1

        for i, jump in enumerate(nums):
            if i > max_reach:  # can't even reach this index
                return False
            max_reach = max(max_reach, i + jump)
            if max_reach >= last_index:
                return True
        
        return False