class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        options = {'(': ')', '{': '}', '[': ']'}

        for b in s:
            if b in options:
                st.append(b)
            else:
                if st and b == options[st[-1]]:
                    st.pop()
                else:
                    return False
        return not st
                       