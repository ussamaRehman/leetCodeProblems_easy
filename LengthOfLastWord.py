# Problem:
# Given a string s consisting of words and spaces, return the length of 
# the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
#
# Approach:
# - Traverse the string from the end.
# - Skip any trailing spaces.
# - Count characters of the last word until a space or the beginning is reached.
#
# Solution:
# - This approach avoids using extra space (no list split).
# - Time complexity: O(n), where n is the length of the string.
# - Space complexity: O(1), uses constant extra space.

from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Start from the end of the string
        i = len(s) - 1
        length = 0

        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Count characters of the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length

sol = Solution()
print(sol.lengthOfLastWord('Hello World'))  # Output: 5
print(sol.lengthOfLastWord('   fly me   to   the moon  '))  # Output: 4
print(sol.lengthOfLastWord('luffy is still joyboy'))  # Output: 6
