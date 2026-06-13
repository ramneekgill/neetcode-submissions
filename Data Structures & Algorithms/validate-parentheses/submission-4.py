class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        options = {'(': ')', '{': '}', '[': ']'}

        for b in s:
            if b in options:
                st.append(b)
            else:
                if st:
                    opening = st.pop()
                    if options[opening] != b:
                        return False
                else:
                    return False
        return not st
                       