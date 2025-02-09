import random
from typing import List

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.valid_count = n - len(blacklist)
        self.blacklist_map = {}
        blacklist_set = set(blacklist)

        # Mapping blacklisted indices to valid numbers in range [valid_count, n)
        last = n - 1
        for b in blacklist:
            if b < self.valid_count:  # Only remap elements in range [0, valid_count - 1]
                while last in blacklist_set:
                    last -= 1
                self.blacklist_map[b] = last
                last -= 1

    def pick(self) -> int:
        rand_index = random.randint(0, self.valid_count - 1)
        return self.blacklist_map.get(rand_index, rand_index)


# Example usage:
# obj = Solution(7, [2, 3, 5])
# print(obj.pick())  # Returns a number from {0, 1, 4, 6} with equal probability
