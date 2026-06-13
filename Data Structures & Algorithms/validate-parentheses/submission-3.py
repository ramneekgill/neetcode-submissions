class Solution:
    def isValid(self, s: str) -> bool:
        # ls = []
        # opening_brackets = {'(', '[', '{'}
        # closing_brackets = {')', ']', '}'}
        # brackets = {'()', '[]', '{}'}
        # for ch in s:
        #     if ch in opening_brackets:
        #         ls.append(ch)
        #     elif ch in closing_brackets:
        #         if not ls:
        #             return False
        #         bracket = ls.pop() + ch
        #         if bracket not in brackets:
        #             return False
        # return not ls
        st = []
        opening = {'(', '[', '{'}
        closing = {')', ']', '}'}
        matching = {'()', '[]', '{}'}
        for ch in s:
            if ch in opening:
                st.append(ch)
            elif ch in closing:
                if st:
                    popped = st.pop()
                    full = popped + ch
                    if full not in matching:
                        return False
                else:
                    return False
        return len(st) == 0
            



        