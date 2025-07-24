# Problem:
# Given a string s, return true if it is a palindrome, or false otherwise.
# A phrase is a palindrome if, after converting all uppercase letters into lowercase 
# letters and removing all non-alphanumeric characters, it reads the same forward and backward.

# Approach:
# 1. Iterate through the string and keep only alphanumeric characters.
# 2. Convert all characters to lowercase.
# 3. Check if the cleaned string is equal to its reverse.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = ''.join(c.lower() for c in s if c.isalnum())
        return s_clean == s_clean[::-1]
