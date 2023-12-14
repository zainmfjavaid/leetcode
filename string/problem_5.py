# Problem 5: Longest Palindromic Substring
# Solution Runtime: 5265ms (beats 15.3%)

def longestPalindrome(s: str) -> str:
    max_length = 0
    max_substring = ''
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if j - i + 1 > max_length and substring == substring[::-1]:
                max_substring = substring
                max_length = len(substring)
    return max_substring