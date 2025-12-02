from typing import List, Dict
from collections import defaultdict

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        lines: Dict[int, int] = defaultdict(int)
        for point in points:
            lines[point[1]] += 1
        res, candi = 0, 0
        for val in lines.values():
            a = val * (val - 1) // 2
            res = (res + a * candi) % 1000000007
            candi = (candi + a) % 1000000007
        return res

