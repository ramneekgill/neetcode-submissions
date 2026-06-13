class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 0
        n = len(digits)-1
        digits[n] += 1
        while True and n >= 0:
            num = digits[n]
            num += carry
            carry = 0
            if num > 9:
                digits[n] = 0
                carry = 1
            else:
                digits[n] = num
            if carry == 0:
                break
            n -= 1
        if n < 0:
            digits.reverse()
            digits.append(carry)
            digits.reverse()
        return digits