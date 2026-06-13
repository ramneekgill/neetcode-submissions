class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm = {}
        
        for task in tasks:
            hm[task] = hm.get(task, 0) + 1
        m_heap = [[-hm[task], task] for task in hm]
        heapq.heapify(m_heap)

        ls = []
        for task in hm:
            ls.append([hm[task], task])
        ls.sort()

        t_cycles = 0
        cur_delay = 0
        while len(ls):
            tmp_ls = []
            o_freq, o_t = ls.pop()
            o_freq -= 1
            if o_freq > 0:
                tmp_ls.append([o_freq, o_t])
                cur_delay = n
            t_cycles += 1
            i = len(ls)-1
            
            while i >= 0 and cur_delay > 0:
                freq, t = ls.pop()
                freq -= 1
                cur_delay -= 1
                t_cycles += 1
                if freq > 0:
                    tmp_ls.append([freq, t])
                i-=1
            while cur_delay > 0:
                t_cycles += 1
                cur_delay -= 1
            ls += tmp_ls
            ls.sort()
        return t_cycles
        



            
                

                
            





        