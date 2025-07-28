from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        Problem:
        Given a sorted list of unique integers, return the smallest sorted list of ranges that cover all the numbers.

        Approach:
        Use two pointers:
        - One to mark the start of a range.
        - Iterate through the list, and when a non-consecutive number is found or we reach the end, close the range.
        
        Time Complexity: O(n)
        Space Complexity: O(1) extra (output list not counted)
        """
        if not nums:
            return []

        ranges = []
        start = 0

        for i in range(1, len(nums) + 1):
            # If end of list or break in consecutive sequence
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                if start == i - 1:
                    ranges.append(str(nums[start]))
                else:
                    ranges.append(f"{nums[start]} -> {nums[i - 1]}")
                start = i  # start new range

        return ranges

sol = Solution()

nums = [0,2,3,4,6,8,9]
                             
print(sol.summaryRanges(nums))