# Solution Runtime: 61ms (beats 86.4%)

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    r_dict = {}
    for i, num in enumerate(nums):
        remainder = target - num
        if remainder in r_dict:
            return [i, r_dict[remainder]]
        else:
            r_dict[num] = i
            
if __name__ == '__main__':
    print(two_sum([3,2,4], 6))