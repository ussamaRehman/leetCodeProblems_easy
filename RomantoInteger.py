# Problem:
# Convert a Roman numeral string into an integer.
# Example: "MCMXCIV" => 1994

# Approach:
# Use a dictionary to map Roman symbols to integers.
# Loop through the string while comparing each character with the next.
# If a smaller value comes before a larger one, subtract it.
# Otherwise, add the value to the result.

# Solution:
# Efficient one-pass solution using pointer comparison.

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,    'V': 5,    'X': 10,
            'L': 50,   'C': 100,  'D': 500,
            'M': 1000
        }

        result = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                result += roman_to_int[s[i + 1]] - roman_to_int[s[i]]
                i += 2
            else:
                result += roman_to_int[s[i]]
                i += 1

        return result
sol = Solution()
print(sol.romanToInt("MCMXCIV"))  # Output: 1994
print(sol.romanToInt("LVIII"))    # Output: 58
print(sol.romanToInt("III"))      # Output: 3