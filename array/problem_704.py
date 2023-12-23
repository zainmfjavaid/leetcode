# Problem 704: Binary Search
# Solution Runtime: 193ms (beats 99.2%)

from typing import List

def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        center = (left + right) // 2
        if nums[center] > target:
            right -= 1
        elif nums[center] < target:
            left += 1
        else:
            return center
    return -1