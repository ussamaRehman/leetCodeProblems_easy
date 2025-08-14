# Problem: Integer to Roman
# Given an integer, convert it to a Roman numeral.
# Rules:
# - Symbols are placed from largest to smallest from left to right.
# - Use subtractive notation for 4, 9, 40, 90, 400, 900.
# - Only I, X, C, and M can repeat at most three times in a row.

# Approach:
# - Use a list of tuples (value, symbol) sorted from largest to smallest.
# - Iterate over the list and subtract values from the number while appending symbols to the result.
# - Stop when the number is reduced to zero.

# Time Complexity: O(1) 
# (The list of Roman mappings is constant length — at most ~13 elements, 
# so operations are bounded.)
# Space Complexity: O(1) 
# (Only a few extra variables are used regardless of input size.)

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I")
        ]
        
        result = []

        for value, symbol in roman_map:
            # Append symbol while we can subtract its value
            while num >= value:
                result.append(symbol)
                num -= value
        
        return "".join(result)