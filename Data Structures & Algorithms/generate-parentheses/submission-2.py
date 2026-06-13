class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(opening, closing, cur):

            if len(cur) == n*2:
                res.append(cur)
                return
            
            if opening < n:
                backtrack(opening +1, closing, cur + '(')
            if opening > closing:
                backtrack(opening, closing+1, cur + ')')
        
        backtrack(0,0,'')
        return res