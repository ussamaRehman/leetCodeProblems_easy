from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Problem:
        Given two strings s and t, return True if t is an anagram of s, and False otherwise.
        An anagram is a word formed by rearranging the letters of another word using all the original letters exactly once.

        Approach:
        - Use collections.Counter to count the frequency of each character in both strings.
        - Compare the two Counter dictionaries: if they are equal, s and t are anagrams.

        Why This Works:
        - Counter works on any iterable (including strings).
        - It returns a dictionary-like object with character frequencies.
        - Two strings are anagrams if and only if their character counts match.

        Unicode Support:
        - This method works for all Unicode characters, including non-ASCII characters.

        Time Complexity: O(n)
        - Where n is the length of the string.
        - Both strings are traversed once to count characters.

        Space Complexity: O(1) 
        - Since the alphabet size is fixed (for English lowercase, it's 26), space is constant.
        - For general Unicode input, space would be O(k), where k is number of unique characters.
        """

        return Counter(s) == Counter(t)