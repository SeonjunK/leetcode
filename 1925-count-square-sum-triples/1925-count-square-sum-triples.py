class Solution:
    def countTriples(self, n: int) -> int:
        s = set()
        i = 2
        while i ** 2 < n:
            for j in range(1, i):
                k = 1
                while (i ** 2 + j ** 2) * k <= n:
                    # print(i, j, k)
                    # print(f'{(i ** 2 + j ** 2) * k} = {(i ** 2 - j ** 2) * k} + {2 * i * j * k}')
                    a = (i ** 2 - j ** 2) * k
                    b = 2 * i * j * k
                    c = (i ** 2 + j ** 2) * k
                    s.add(tuple([a, b, c]))
                    s.add(tuple([b, a, c]))
                    k += 1
            i += 1
        # print(res)
        return len(s)
