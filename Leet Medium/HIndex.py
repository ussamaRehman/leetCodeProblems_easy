from typing import List

class Solution:
    # Problem:
    # Given an array citations where citations[i] is the number of citations for the i-th paper,
    # return the researcher's h-index. The h-index is the largest h such that the researcher has
    # at least h papers with at least h citations each.

    # Approach:
    # - Sort the citations in descending order.
    # - Scan from left to right; let i (1-based) be the number of papers considered so far.
    # - The largest i such that citations[i-1] >= i is the h-index.
    #
    # Example: citations = [3,0,6,1,5] -> sorted: [6,5,3,1,0]
    # i=1 (6>=1), i=2 (5>=2), i=3 (3>=3), i=4 (1<4) -> answer = 3.

    # Complexity:
    # - Time: O(n log n) due to sorting.
    # - Space: O(1) extra (ignoring the input list being sorted in place).
    #   (If you need O(n) time, you can use a counting/bucket approach.)

    def hIndex(self, citations: List[int]) -> int:
        # Sort descending
        citations.sort(reverse=True)

        # i is 1-based to match "at least i papers have >= i citations"
        for i, c in enumerate(citations, start=1):
            if c < i:
                # We've gone past the valid h; previous i-1 is the answer
                return i - 1

        # All positions satisfied c >= i, so h is total number of papers
        return len(citations)