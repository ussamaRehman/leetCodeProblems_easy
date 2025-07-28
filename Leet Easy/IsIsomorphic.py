# Problem: Isomorphic Strings
# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t,
# with a one-to-one mapping between every character of s to every character of t.

# Approach:
# Use two hash maps (dictionaries) to track character mappings from s -> t and t -> s.
# For each character pair (s[i], t[i]), ensure the mapping is consistent in both directions.

# Solution:
# Traverse both strings simultaneously using zip().
# Check if characters have already been mapped and verify consistency.
# If any inconsistency is found, return False.
# If all mappings are consistent, return True.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False  # Strings of different lengths can't be isomorphic

        s_to_t = {}  # Map from characters in s to characters in t
        t_to_s = {}  # Map from characters in t to characters in s

        for c1, c2 in zip(s, t):
            # Check if there's a previous mapping for c1 -> c2
            if c1 in s_to_t:
                if s_to_t[c1] != c2:
                    return False  # Inconsistent mapping
            else:
                s_to_t[c1] = c2

            # Check if there's a previous mapping for c2 -> c1
            if c2 in t_to_s:
                if t_to_s[c2] != c1:
                    return False  # Inconsistent reverse mapping
            else:
                t_to_s[c2] = c1

        return True  # All characters mapped consistently