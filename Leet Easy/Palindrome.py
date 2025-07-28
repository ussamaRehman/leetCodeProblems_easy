# Problem: Given an integer x, 
# return true if x is a palindrome, and false otherwise.

# Approach: we will be checking if the integer x is a palindrome or not 
# without converting it into a string

# Solution: We will first check if the integer is negaive, if it is we can 
# simply return False, as all negative numbers are never palindrome.
# After that, we will be using modulus and floor division in while loop to
# check if it is a palindrome or not

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        original = x
        reversed_num = 0

        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        return original == reversed_num
sol = Solution()
print(sol.isPalindrome(121))   # True
print(sol.isPalindrome(-121))  # False
print(sol.isPalindrome(10))    # False