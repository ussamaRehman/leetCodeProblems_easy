from typing import List

class Solution:
    # Problem:
    # Return an array answer where answer[i] is the product of all elements of nums except nums[i],
    # without using division, in O(n) time and O(1) extra space (excluding the output array).

    # Approach:
    # Two passes with prefix/suffix products:
    # - First pass (left -> right): res[i] = product of all elements before i.
    # - Second pass (right -> left): multiply res[i] by product of all elements after i.
    # This naturally handles zeros without special cases.

    # Complexity:
    # - Time: O(n)
    # - Space: O(1) extra (res is the required output array)

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # Prefix products
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res