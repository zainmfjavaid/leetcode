# Problem 238: Product of Array Except Self
# Solution Runtime: 189ms (beats 78.3%)

from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    products = [1] * len(nums)
    for i in range(1, len(nums)):
        products[i] = products[i - 1] * nums[i - 1]

    suffix = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        products[i] *= suffix
        suffix *= nums[i]
    
    return products