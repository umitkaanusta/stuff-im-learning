class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # m: rows
        # n: cols
        if (m * n) != len(original):
            return []
        mtx = [[None for _ in range(n)] for _ in range(m)]
        i = 0
        j = 0
        for idx in range(len(original)):
            mtx[i][j] = original[idx]
            j += 1
            if j == n:
                j = 0
                i += 1
        return mtx
