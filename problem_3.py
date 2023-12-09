# Solution Runtime: 53ms (beats 88.7%)

def length_of_longest_substring(s: str) -> int:
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

if __name__ == '__main__':
    print(length_of_longest_substring('pwwkew'))