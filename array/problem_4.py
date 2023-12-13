# Problem 4: Median of Two Sorted Arrays
# Solution Runtime: 89ms (beats 65.2%)

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = list(sorted(nums1 + nums2))
        
        if len(merged_list) == 1:
            return merged_list[0]
        elif len(merged_list) == 2:
            return (merged_list[0] + merged_list[1]) / 2
        
        if len(merged_list) % 2 != 0:
            middle = len(merged_list) // 2
            return merged_list[middle]
        else:
            first_point = len(merged_list) // 2
            second_point = first_point - 1
            return (merged_list[first_point] + merged_list[second_point]) / 2