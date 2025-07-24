# Problem: Plus One

# Approach:
# - Iterate from the last digit to the first.
# - If the digit is less than 9, simply increment it and return.
# - If the digit is 9, set it to 0 and continue.
# - If all digits are 9, insert 1 at the beginning to handle carry-over.

# Time Complexity: O(n) where n is the length of the digits list.
# Space Complexity: O(1) excluding the input and output, as the operation is in-place.
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Traverse the list in reverse to handle carry from the least significant digit
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        # If loop completes, it means all digits were 9. Insert 1 at the start.
        digits.insert(0, 1)
        return digits

# Test case
digits = [9]
sol = Solution()
result = sol.plusOne(digits)
# Output the result
print(result)