# Problem 217: Contains Duplicate
# Solution Runtime: 470ms (beats 76.4%)

from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))