from collections import defaultdict

class Solution:
    def initiate_illuminated(self, n: int, lamps: List[List[int]]):
        row = defaultdict(int)
        col = defaultdict(int)
        diag1 = defaultdict(int)
        diag2 = defaultdict(int)
        lampdict = {tuple(lamp): True for lamp in lamps}
        for lamp_i, lamp_j in lampdict:
            row[lamp_i] += 1
            col[lamp_j] += 1
            diag1[lamp_i - lamp_j] += 1
            diag2[lamp_i + lamp_j] += 1
        return row, col, diag1, diag2, lampdict
    
    def execute_queries(self, n: int, queries: List[List[int]], row: dict, col: dict, diag1: dict, diag2: dict, lampdict: dict):
        answer = []
        for query_i, query_j in queries:
            answer.append(int(row[query_i] > 0 or col[query_j] > 0 or
                         diag1[query_i - query_j] > 0 or diag2[query_i + query_j] > 0))
            # clear adjacent squares
            for i, j in ((-1, -1), (-1, 0), (-1, 1), 
                         (0, -1), (0, 0), (0, 1),
                        (1, -1), (1, 0), (1, 1)):
                adj_i, adj_j = query_i + i, query_j + j
                if 0 <= adj_i < n and 0 <= adj_j < n:
                    if (adj_i, adj_j) in lampdict and lampdict[(adj_i, adj_j)]:
                        row[adj_i] -= 1
                        col[adj_j] -= 1
                        diag1[adj_i - adj_j] -= 1
                        diag2[adj_i + adj_j] -= 1
                        lampdict[(adj_i, adj_j)] = False
        return answer
            
    
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        # just keep the number of rows, since only one lamp is enough to illuminate a row/col/diagonal
        row_, col_, diag1_, diag2_, lampdict_ = self.initiate_illuminated(n, lamps)
        return self.execute_queries(n, queries, row_, col_, diag1_, diag2_, lampdict_)
