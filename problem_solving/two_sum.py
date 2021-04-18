from typing import List
from collections import deque


def twoSum(nums: List[int], target: int) -> List[int]:
    # Total: O(nlogn)
    nums_org = nums
    nums = sorted(nums)  # O(nlogn)
    i = 0
    j = len(nums) - 1
    while i < j:  # O(n)
        sum_ = nums[i] + nums[j]
        if sum_ == target:
            break
        if sum_ < target:
            i += 1
        if sum_ > target:
            j -= 1
    return [k for k in range(len(nums_org)) if nums_org[k] in (nums[i], nums[j])]  # O(n)


def twoSumOptimized(nums: List[int], target: int) -> List[int]:
    # Total: O(n)
    table = {num: deque([]) for num in nums}
    for idx, num in enumerate(nums):
        table[num].append(idx)
    for num in nums:
        if num in table and (target - num) in table:
            num_ind = table[num].popleft()  # deque.popleft() is O(1)
            if len(table[target - num]) > 0:  # len(deque) is O(1)
                return [num_ind, table[target - num].popleft()]


if __name__ == '__main__':
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert twoSum([3, 2, 4], 6) == [1, 2]
    assert twoSum([3, 3], 6) == [0, 1]
    assert twoSum([2, 5, 5, 11], 10) == [1, 2]

    assert twoSumOptimized([2, 7, 11, 15], 9) == [0, 1]
    assert twoSumOptimized([3, 2, 4], 6) == [1, 2]
    assert twoSumOptimized([3, 3], 6) == [0, 1]
    assert twoSumOptimized([2, 5, 5, 11], 10) == [1, 2]
