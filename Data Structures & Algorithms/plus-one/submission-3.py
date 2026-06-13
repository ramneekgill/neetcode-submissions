class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # If increment the last digit by one and if it's not 9 I return the list
        # immediatley. If the last digit is a 9 I loop until it isn't a 9 and 
        #I return immediately. I modify in place val to 0 and carry = True
        n = len(digits)-1
        if digits[n] < 9:
            digits[n] += 1
            return digits
        
        #last digit is 9
        #have to loop until carry = False
        carry = True
        while carry:
            if n >= 0:
                num = digits[n] + 1
                if num == 10:
                    digits[n] = 0
                    carry = True
                else:
                    digits[n] = num
                    carry = False
            else:
                return [1] + digits
            n-=1
        return digits






            
            
        