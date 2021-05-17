def maxSubArray(self, nums: List[int]) -> int:
    # DP solution - O(n)
    max_sum = nums[0]
    curr = nums[0]
    prev = nums[0]
    for i in range(1, len(nums)):
        curr = max(nums[i], nums[i] + prev)
        if curr > max_sum:
            max_sum = curr
        prev = curr
    return max_sum   
 
