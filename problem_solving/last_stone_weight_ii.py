class Solution:
	# goal: partition the array to two subsets such that abs(sum(subset1) - sum(subset2)) is minimized
	# in the ideal case, this can be achieved by having sum(subset1) = sum(subset2) = sum(array) / 2, 
	#	this is our constraint in 0-1 knapsack optimization.
    def lastStoneWeightII(self, stones: List[int]) -> int:
        max_subset_sum = sum(stones) // 2
        dp = [True] + [False for _ in range(max_subset_sum)]
        for stone in stones:
            for possible_subset_sum in range(max_subset_sum, -1, -1):
                if possible_subset_sum - stone >= 0 and dp[possible_subset_sum - stone]:
                    dp[possible_subset_sum] = True
        for possible_subset_sum in range(max_subset_sum, -1, -1):
            if dp[possible_subset_sum]:
                return sum(stones) - 2 * possible_subset_sum
        
