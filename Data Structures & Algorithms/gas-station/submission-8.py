class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i]-cost[i])
        
        if sum(diff) < 0:
            return -1
        
        idx = -1
        running_sum = float('-inf')
        print(diff)
        for i in range(len(diff)):
            if diff[i] >= 0 and running_sum < 0:
                idx = i
                running_sum = 0
            running_sum += diff[i]
        return idx

            
            
            




        