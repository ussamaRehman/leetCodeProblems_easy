import random

class RandomizedSet:
    # Problem:
    # Implement insert, remove, and getRandom in average O(1) time.

    # Approach:
    # - Maintain:
    #   1) arr: list of values for O(1) random index selection
    #   2) pos: dict mapping value -> index in arr for O(1) membership and swaps
    # - insert(x): if x not in pos, append to arr and record index in pos
    # - remove(x): if x in pos, swap arr[pos[x]] with arr[-1], update positions, pop last
    # - getRandom(): return random choice of arr via random.randint
    #
    # Complexity:
    # - Time: O(1) average for all operations
    # - Space: O(n)

    def __init__(self):
        self.arr = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        idx = self.pos[val]
        last = self.arr[-1]
        # move last into idx
        self.arr[idx] = last
        self.pos[last] = idx
        # remove tail + mapping
        self.arr.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        # LeetCode guarantees getRandom is called when set is non-empty
        return self.arr[random.randint(0, len(self.arr) - 1)]