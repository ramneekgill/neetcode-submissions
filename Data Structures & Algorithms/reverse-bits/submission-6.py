class Solution:
    def reverseBits(self, n: int) -> int:
        b = format(n, '032b')
        b = b[::-1]
        return int(b,2)

        