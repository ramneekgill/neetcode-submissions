class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }
        dic2 = {
            0: "0",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9"
        }
        d_num1 = 0
        for i in range(len(num1)):
            d_num1 = (d_num1 * 10) + dic[num1[i]]
        
        d_num2 = 0
        for i in range(len(num2)):
            d_num2 = (d_num2 * 10) + dic[num2[i]]
        
        total = d_num1*d_num2
        res = []
        if total == 0:
            return '0'
        while total:
            num = total%10
            total = total//10
            res.append(dic2[num])
        
        res.reverse()
        return ''.join(res)

        


        