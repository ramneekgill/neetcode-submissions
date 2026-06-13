class Solution:
    def reverseBits(self, n: int) -> int:
        b = format(n, '032b')
        b = b[::-1]
        b = ''.join(b)
        return int(b,2)

        