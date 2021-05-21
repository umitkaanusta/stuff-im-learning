class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        max_so_far = nums[0]
        min_so_far = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_so_far, min_so_far = min_so_far, max_so_far
            max_so_far = max(nums[i], nums[i] * max_so_far)
            min_so_far = min(nums[i], nums[i] * min_so_far)
            max_prod = max(max_prod, max_so_far)
        return max_prod
