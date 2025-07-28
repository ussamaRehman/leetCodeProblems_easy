class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Problem:
        A happy number is a number defined by the following process:
        - Starting with any positive integer, replace the number by the sum of the squares of its digits.
        - Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1.
        - Numbers for which this process ends in 1 are happy numbers.

        Approach:
        - Use a set to store numbers we've seen before to detect cycles.
        - At each step, replace the number with the sum of the squares of its digits.
        - If we see the same number again, we are in a loop → return False.
        - If we reach 1, it's a happy number → return True.

        Time Complexity: O(log n)
        - Each iteration reduces the number roughly proportional to the number of digits (log n).

        Space Complexity: O(log n)
        - In the worst case, we store up to log n seen numbers.
        """

        seen = set()

        while n != 1:
            # Calculate the sum of the squares of the digits
            n = sum(int(digit) ** 2 for digit in str(n))

            # If we've seen this number before, it's a cycle
            if n in seen:
                return False

            # Mark this number as seen
            seen.add(n)

        # If we reach 1, it's a happy number
        return True