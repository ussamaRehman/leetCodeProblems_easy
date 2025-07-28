# Problem: Is Subsequence
# Approach: Two-pointer technique
# Time Complexity: O(n) where n = len(t)
# Space Complexity: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # Pointer for s

        for char in t:
            if i < len(s) and s[i] == char:
                i += 1

        return i == len(s)