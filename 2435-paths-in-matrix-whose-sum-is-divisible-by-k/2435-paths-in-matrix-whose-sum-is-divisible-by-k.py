from typing import List

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                num = grid[i][j]
                grid[i][j] = [0 for _ in range(k)]
                if i == 0 and j == 0:
                    grid[i][j][num % k] = 1
                elif i == 0:
                    for l, prev in enumerate(grid[i][j-1]):
                        grid[i][j][(l + num) % k] = prev % (10**9 + 7)
                elif j == 0:
                    for l, prev in enumerate(grid[i-1][j]):
                        grid[i][j][(l + num) % k] = prev % (10**9 + 7)
                else:
                    for l, prev in enumerate(grid[i][j-1]):
                        grid[i][j][(l + num) % k] = prev % (10**9 + 7)
                    for l, prev in enumerate(grid[i-1][j]):
                        grid[i][j][(l + num) % k] += prev
                        grid[i][j][(l + num) % k] %= (10**9 + 7)
        return grid[-1][-1][0]