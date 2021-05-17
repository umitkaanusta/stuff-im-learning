def minCostClimbingStairs(cost: List[int]) -> int:
    # DP - O(n)
    prev_prev = cost[0]
    prev = cost[1]
    for i in range(2, len(cost)):
        curr = cost[i] + min(prev, prev_prev)
        prev_prev = prev
        prev = curr
    return min(prev, prev_prev)
