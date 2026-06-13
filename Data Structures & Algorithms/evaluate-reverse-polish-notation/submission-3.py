class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a/b),
        }


        st = []
        for token in tokens:
            if token in operators:
                operand_b = st.pop()
                operand_a = st.pop()
                res = operators[token](operand_a,operand_b) 
                st.append(res)
            else:
                st.append(int(token))
        
        return st[0]

        
        


        