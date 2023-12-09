# Solution Runtime: 50ms (beats 91.7%)

"""One Liner"""
def is_palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]

"""Efficient"""
def is_palindrome(x: int) -> bool:
    sx = str(x)
    length = len(sx)
    for i in range(length):
        if sx[i] != sx[length - i - 1]:
            return False
    return True