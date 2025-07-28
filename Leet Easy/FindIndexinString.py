    # Problem:
    # Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
    # or -1 if needle is not part of haystack.

    # Approach:
    # Use Python's built-in string.find() method to find the first index of the needle in the haystack.
    # If not found, .find() returns -1, which matches the problem's expected return.

    # Solution:
    # Call haystack.find(needle) and return the result.
    # No need to check for None, since .find() never returns None — it returns -1 on failure.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result = haystack.find(needle)
        return result

sol = Solution()

haystack, needle = "sadbutsad",   "sad" 
result = sol.strStr(haystack, needle)
print(result)


