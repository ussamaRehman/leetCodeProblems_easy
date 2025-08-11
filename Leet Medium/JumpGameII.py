class Solution:
    def jump(self, nums):
        """
        Problem:
        Given an array nums where each element represents the maximum jump length from that position,
        return the minimum number of jumps required to reach the last index.

        Approach:
        - Use a greedy O(n) approach:
            - Track the farthest reachable index at each step.
            - Track the current jump boundary (end of current range).
            - When we reach the current jump boundary, increment jump count and
              extend the boundary to the farthest reachable index so far.

        Complexity:
        - Time: O(n) — Single pass through nums.
        - Space: O(1) — No extra space used beyond variables.
        """
        jumps = 0
        end = 0
        farthest = 0

        # We don't check the last index because we stop when we reach it
        for i in range(len(nums) - 1):
            # Update farthest reach
            farthest = max(farthest, i + nums[i])

            # If we reached the end of the current jump's range
            if i == end:
                jumps += 1
                end = farthest

        return jumps