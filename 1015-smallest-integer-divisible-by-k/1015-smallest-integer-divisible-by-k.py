# 1 * 1 = 1
# 1 % 1
# 2 -> not posible
# 3 * 7 = 21
# 111 % 3
# 4 -> not posible
# 5 -> not posible
# 6 -> not posible
# 7 * 3 = 21
# 111111 % 7
# 9 * 9 = 81
# 111111111 % 9
# 10 -> not posible
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 10 in [0, 2, 4, 5, 6, 8]:
            return -1
        
        n = 0
        i = 1
        while True:
            n = (n * 10 + 1) % k
            if n == 0:
                return i
            i += 1
