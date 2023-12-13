# Problem 20: Valid Parentheses
# Solution Runtime: 33ms (beats 88.7%)

class Solution:
    def isValid(self, s: str) -> bool:
        opens = ['(', '[', '{']
        closes = [')', ']', '}']
        open_close_dict = {opens[i]:closes[i] for i in range(len(opens))}

        curr_opens = []
        for i in range(len(s)):
            if s[i] in open_close_dict:
                curr_opens.append(s[i])
            elif len(curr_opens) > 0:
                match_open = curr_opens[-1]
                if open_close_dict[match_open] != s[i]:
                    return False
                else:
                    curr_opens.pop()
            else:
                return False

        return len(curr_opens) == 0