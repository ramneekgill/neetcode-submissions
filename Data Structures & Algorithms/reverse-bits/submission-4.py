class Solution:
    def reverseBits(self, n: int) -> int:
        b = format(n, '032b')
        b = list(b)
        b.reverse()
        b = ''.join(b)
        return int(b,2)

        