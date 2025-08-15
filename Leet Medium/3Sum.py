class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Problem:
        Given an integer array nums, return all unique triplets [a, b, c] such that:
            a + b + c == 0
        Triplets must be unique (no duplicates in the output).

        Approach (Sort + Two Pointers):
        1) Sort nums to enable two-pointer scanning and easy duplicate skipping.
        2) For each index i, treat nums[i] as the fixed value:
           - If i > 0 and nums[i] == nums[i-1], skip to avoid duplicate triplets starting with same nums[i].
           - Use two pointers L = i+1 and R = n-1 to find pairs summing to -nums[i]:
             * sum = nums[i] + nums[L] + nums[R]
             * If sum == 0: record triplet, move L and R inward while skipping duplicates at L and R.
             * If sum < 0: L += 1 (need a larger value).
             * If sum > 0: R -= 1 (need a smaller value).
        3) Collect all unique triplets.

        Complexity:
        - Time: O(n^2)   (sorting O(n log n) + outer loop with linear two-pointer sweeps)
        - Space: O(1) extra (ignoring the output list)
        """
        nums.sort()
        n = len(nums)
        res: list[list[int]] = []

        for i in range(n):
            # Skip duplicate anchors
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two-pointer search for pairs with nums[i]
            target = -nums[i]
            L, R = i + 1, n - 1

            while L < R:
                s = nums[L] + nums[R]
                if s == target:
                    res.append([nums[i], nums[L], nums[R]])
                    # Skip duplicates on L and R
                    L_val, R_val = nums[L], nums[R]
                    while L < R and nums[L] == L_val:
                        L += 1
                    while L < R and nums[R] == R_val:
                        R -= 1
                elif s < target:
                    L += 1
                else:
                    R -= 1

        return res