class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        for c in [num1,num2]:
            if c == '0':
                return 0
        res = [0]*(len(num1)+len(num2))
        n1,n2 = num1[::-1], num2[::-1]

        for c1 in range(len(n1)):
            for c2 in range(len(n2)):
                res[c1+c2] += int(n1[c1])*int(n2[c2])
                res[c1+c2+1] += res[c1+c2]//10
                res[c1+c2] %= 10

        res = res[::-1]
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1
        res = map(str,res[start:])

        res = ''.join(res)
        return res



        