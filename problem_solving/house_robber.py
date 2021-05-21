class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        nums = [0] + nums
        prev_prev = 0
        prev = nums[1]
        curr = None
        for i in range(2, len(nums)):
            curr = max(nums[i] + prev_prev, prev)
            prev_prev = prev
            prev = curr
            i += 1
        return curr
