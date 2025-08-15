class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Problem:
        Given an array height where height[i] is the height of a vertical line at x = i,
        pick two lines i < j to form a container with the x-axis. The container's area is:
            area = (j - i) * min(height[i], height[j]).
        Return the maximum possible area.

        Approach (Two Pointers):
        - Use two pointers L=0 and R=n-1 (widest container initially).
        - At each step, compute area with (L, R).
        - Move the pointer on the *shorter* line inward:
            - This may find a taller line, which can compensate for reduced width.
            - Moving the taller line cannot help since the height is capped by the shorter one.
        - Track the maximum area during the sweep.

        Complexity:
        - Time: O(n) — each pointer moves at most n steps total.
        - Space: O(1) — constant extra space.
        """
        L, R = 0, len(height) - 1
        best = 0

        while L < R:
            h = min(height[L], height[R])
            best = max(best, h * (R - L))
            # Move the pointer at the shorter line
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1

        return best