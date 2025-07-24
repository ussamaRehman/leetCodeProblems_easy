#Problem: ou are given two integer arrays nums1 and nums2, sorted in non-decreasing 
# order, and two integers m and n, representing the number of elements in nums1 
# and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in 
# non-decreasing order.

# The final sorted array should not be returned by the 
# function, but instead be stored inside the array nums1. To accommodate this, nums1 has 
# a length of m + n, where the first m elements denote the elements 
# that should be merged, and the last n elements are set to 0 and should be ignored. 
# nums2 has a length of n.

# Approach:
# - We are given two sorted arrays: nums1 and nums2.
# - nums1 has extra space at the end (filled with zeros) to accommodate all elements from nums2.
# - We merge the arrays from the back using three pointers: 
#     i (end of valid nums1), j (end of nums2), and k (end of total space in nums1).
# - We compare nums1[i] and nums2[j], and place the larger at nums1[k].
# - Continue until all elements from nums2 are merged.
# - If any elements remain in nums2 (and not in nums1), we copy them over.

# Time Complexity: O(m + n) — we traverse both arrays once
# Space Complexity: O(1) — in-place merge without extra space

# Notes:
# - This is an optimal in-place solution.
# - Important to fill from the back to avoid overwriting elements in nums1.

 

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Start filling from the back
        i = m - 1
        j = n - 1
        k = m + n - 1  # Position to fill in nums1

        # Merge in reverse order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If any elements left in nums2, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

sol = Solution()            
nums1 = [1, 2, 3, 0, 0, 0]
sol.merge(nums1, m=3, nums2=[2, 5, 6], n=3)
print(nums1)  # ✅ Output: [1, 2, 2, 3, 5, 6]