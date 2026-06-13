class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #I increment the last digit by one and if it's not 9 I return the list
        # if the last digit is a 9 I loop
        output = []
        curr_num = 0
        carry = False
        for i in range(len(digits)-1,-1,-1):
            if i == len(digits)-1:
                curr_num = digits[i] + 1
            elif carry:
                curr_num = digits[i] + 1
                carry = False
            else:
                curr_num = digits[i]
            
            if curr_num == 10:
                output.append(0)
                carry = True
            else:
                output.append(curr_num)
        if carry:
            output.append(1)
        output.reverse()
        return output
            
            
        