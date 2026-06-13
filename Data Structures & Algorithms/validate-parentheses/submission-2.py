class Solution:
    def isValid(self, s: str) -> bool:
        ls = []
        opening_brackets = {'(', '[', '{'}
        closing_brackets = {')', ']', '}'}
        brackets = {'()', '[]', '{}'}
        for ch in s:
            if ch in opening_brackets:
                ls.append(ch)
            elif ch in closing_brackets:
                if not ls:
                    return False
                bracket = ls.pop() + ch
                if bracket not in brackets:
                    return False
        return not ls
            



        