# Problem 125: Valid Palindrome
# Solution Runtime: 40ms (beats 94.5%)

def isPalindrome(s: str) -> bool:
    s = [char for char in s.lower() if char.isalnum()]
    return s == s[::-1]