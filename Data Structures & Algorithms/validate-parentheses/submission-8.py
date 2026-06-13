class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        hm = {')': '(', ']': '[', '}': '{'}
        for b in s:
            if b in hm:
                if st and hm[b] == st[-1]:
                    st.pop()
                else:
                    return False
            else:
                st.append(b)
        return len(st) == 0

        