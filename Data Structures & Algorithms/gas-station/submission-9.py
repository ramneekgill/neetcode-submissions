class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i]-cost[i])
        

        idx = -1
        running_sum = float('-inf')
        total_sum = 0
        for i in range(len(diff)):
            total_sum += diff[i]
            if diff[i] >= 0 and running_sum < 0:
                idx = i
                running_sum = 0
            running_sum += diff[i]
        return idx if total_sum >= 0 else -1

            
            
            




        