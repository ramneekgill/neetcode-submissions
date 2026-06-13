class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_dict = {
            "*": lambda a,b: a*b,
            "+": lambda a,b: a+b,
            "-": lambda a,b: a-b,
            "/": lambda a,b: int(float(a) / b),
        }
        ls = []
        for token in tokens:
            if token.lstrip('-').isdigit():
                ls.append(int(token))
            else:
                b = ls.pop()
                a = ls.pop()
                val = operator_dict[token](a,b)
                ls.append(val)
        return ls.pop()



        