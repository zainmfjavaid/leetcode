# Problem 53: Maximum Subarray
# Solution Runtime: 562ms (beats 92.6%)

from typing import List

def maxSubArray(nums: List[int]) -> int:
    max_sum = nums[0]
    curr_sum = 0
    for i in range(len(nums)):
        if nums[i] > curr_sum and curr_sum < 0:
            curr_sum = 0
        curr_sum += nums[i]
        
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum