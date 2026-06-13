class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas = gas[:] + gas[:]
        cost = cost[:] + cost[:]
        curr_val = 0
        curr_idx = 0
        for i in range(0,len(gas)):
            if curr_val < 0 and i<(len(gas)//2):
                curr_val = 0
                curr_idx = i
            if i>=(len(gas)//2) and curr_val < 0:
                return -1
            curr_val += (gas[i] - cost[i])
        return curr_idx

        