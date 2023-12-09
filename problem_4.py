# Solution Runtime: 89ms (beats 65.0%)

from typing import List

def find_median_sorted_array(nums1: List[int], nums2: List[int]) -> float:
    merged_list = nums1 + nums2
    merged_list.sort()
    merged_length = len(merged_list)


    if merged_length % 2 == 0:
        first_point = merged_length // 2
        return (merged_list[first_point] + merged_list[first_point - 1]) / 2
    else:
        return merged_list[merged_length // 2]
    
if __name__ == '__main__':
    print(find_median_sorted_array([1,2], [3,4]))