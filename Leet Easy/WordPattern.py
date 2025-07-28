"""
Problem:
Determine if the string 's' follows the same pattern as 'pattern'.
Each character in 'pattern' must map to exactly one word in 's', and vice versa.

Approach:
- Split the string into words.
- If lengths don't match, return False.
- Use two dictionaries to maintain bijective (one-to-one) mapping:
    pattern → word and word → pattern
- For each pair (pattern_char, word), ensure both mappings are consistent.

Time Complexity: O(n), where n = length of pattern / number of words
Space Complexity: O(n), for the two hash maps
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
 
        words = s.split()

        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for c, w in zip(pattern, words):
            if (c in char_to_word and char_to_word[c] != w) or \
               (w in word_to_char and word_to_char[w] != c):
                return False
            char_to_word[c] = w
            word_to_char[w] = c

        return True