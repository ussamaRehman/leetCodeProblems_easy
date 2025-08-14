class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Problem:
        Given a string s and an integer numRows, write the characters in a zigzag pattern across numRows
        (moving down then diagonally up repeatedly), and return the string formed by reading the rows left to right.

        Approach (Row-Simulation / Buckets):
        - If numRows == 1 or numRows >= len(s), the zigzag is just s.
        - Maintain a list of strings 'rows' of length numRows.
        - Walk through s with a pointer 'r' indicating the current row, and a direction 'step' (+1 down, -1 up).
        - Append each character to rows[r], flip direction when hitting the top (r == 0) or bottom (r == numRows-1).
        - Join all rows at the end.

        Complexity:
        - Time: O(n), where n = len(s). Each char is processed once.
        - Space: O(n) for the rows content (output-sized). Auxiliary overhead O(numRows).
        """

        if numRows == 1 or numRows >= len(s):
            return s

        rows = ["" for _ in range(numRows)]
        r, step = 0, 1  # start at top row, moving downward

        for ch in s:
            rows[r] += ch
            # Reverse direction at the top or bottom
            if r == 0:
                step = 1
            elif r == numRows - 1:
                step = -1
            r += step

        return "".join(rows)