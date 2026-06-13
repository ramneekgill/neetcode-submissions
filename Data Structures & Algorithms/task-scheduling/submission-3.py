class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]

        q = deque()
        time = 0
        while max_heap or q:
            time += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt, time+n])
            else:
                time = q[0][1]
            if q and time == q[0][1]:
                heapq.heappush(max_heap, q.popleft()[0])
        return time



        



            
                

                
            





        