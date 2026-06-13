class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # if endWord not in wordList:
        #     return 0
        adj_ls = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                adj_ls[pattern].append(word)
        
        q = deque([beginWord])
        visit = set(beginWord)
        wordList.append(beginWord)
        level = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return level
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighbor in adj_ls[pattern]:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            q.append(neighbor)
            level += 1
        return 0
                



        