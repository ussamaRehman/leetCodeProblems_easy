

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Problem:
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
        determine if the input string is valid.

        A string is valid if:
        - Open brackets are closed by the same type of brackets.
        - Open brackets are closed in the correct order.

        Approach:
        - Use a stack to store opening brackets.
        - When a closing bracket is encountered, check for a matching opening bracket at the top of the stack.
        - If the stack is empty or mismatched at any point, return False.

        Time Complexity: O(n), where n is the length of the string.
        Space Complexity: O(n), in worst case all characters are opening brackets.
        """
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        return not stack