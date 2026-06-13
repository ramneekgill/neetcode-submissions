class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                adj[pattern].append(word)
        
        q = deque([beginWord])
        visited = set([beginWord])
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    for neighbor in adj[pattern]:
                        if neighbor not in visited:
                            if neighbor == endWord:
                                return res+1
                            visited.add(neighbor)
                            q.append(neighbor)
            res += 1
        return 0
                