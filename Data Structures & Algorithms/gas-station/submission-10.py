class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i]-cost[i])
        

        idx = 0
        running_sum = 0
        total_sum = 0
        for i in range(len(diff)):
            total_sum += diff[i]
            running_sum += diff[i]
            if running_sum < 0:
                idx = i+1
                running_sum = 0
            
        return idx if total_sum >= 0 else -1

            
            
            




        