from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn)
        intervals.sort(key=lambda x : x[0])

        # O(n)
        i = 1
        while i < len(intervals):
            if intervals[i-1][1] >= intervals[i][0]:
                intervals[i][0] = intervals[i-1][0]
                intervals[i][1] = max(intervals[i-1][1], intervals[i][1])
                intervals[i-1] = None
            i += 1
        
        # O(n)
        return list(filter(lambda x : x is not None, intervals))