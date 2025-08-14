class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Problem:
        Given a string s, reverse the order of words. 
        A word is defined as a sequence of non-space characters. 
        Output should have no leading/trailing spaces, and words separated by a single space.

        Approach:
        - Convert string to list of characters for in-place operations (O(1) extra space).
        - Reverse the entire list.
        - Reverse each individual word to restore their correct spelling.
        - Remove extra spaces (leading, trailing, multiple between words).

        Complexity:
        - Time: O(n) -> Each character visited constant times.
        - Space: O(1) extra -> In-place character swaps.
        """

        chars = list(s)  # Convert string to list (mutable)

        # Helper function to reverse chars between left & right
        def reverse(l, r):
            while l < r:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1

        n = len(chars)

        # 1. Reverse the entire string
        reverse(0, n - 1)

        # 2. Reverse each word individually
        start = 0
        for end in range(n + 1):
            if end == n or chars[end] == ' ':
                reverse(start, end - 1)
                start = end + 1

        # 3. Clean up spaces (keep single spaces between words)
        i = 0  # slow pointer
        for j in range(n):
            if chars[j] != ' ':
                chars[i] = chars[j]
                i += 1
            elif i > 0 and chars[i - 1] != ' ':
                chars[i] = ' '
                i += 1

        # Remove trailing space if exists
        if i > 0 and chars[i - 1] == ' ':
            i -= 1

        return ''.join(chars[:i])