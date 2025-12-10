from typing import List

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        res = 1
        for i in range(1, len(complexity)):
            if complexity[i] <= complexity[0]:
                return 0
            res = (res * i) % ((10 ** 9) + 7)
        return res