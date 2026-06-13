class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] *(n+1)
        for i in range(len(output)):
            num = 0
            b = i
            while b:
                b &= (b-1)
                num+=1
            output[i] = num
        return output


        