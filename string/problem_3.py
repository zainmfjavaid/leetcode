# Problem 3: Longest Substring Without Repeating Characters
# Solution Runtime: 53ms (beats 88.2%)

def lengthOfLongestSubstring(s: str) -> int:
    window = set()
    left = 0
    longest_len = 0

    for right in range(len(s)):
        while s[right] in window:
            window.remove(s[left])
            left += 1
        window.add(s[right])
        longest_len = max(longest_len, right - left + 1)

    return longest_len