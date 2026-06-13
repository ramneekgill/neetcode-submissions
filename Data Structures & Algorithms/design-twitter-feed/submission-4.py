class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set)
        self.tweet_map = defaultdict(list)
        self.time = 0

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([tweetId, self.time])
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxheap = []
        self.follow_map[userId].add(userId)
        for user_id in self.follow_map[userId]:
            if user_id in self.tweet_map:
                tweet_list = self.tweet_map[user_id]
                index = len(tweet_list)-1
                tweetId, time = tweet_list[index]
                maxheap.append([time,tweetId,user_id,index-1])
        
        heapq.heapify(maxheap)
        while maxheap and len(res) < 10:
            time,tweetId,user_id,index = heapq.heappop(maxheap)
            res.append(tweetId)
            if index >= 0:
                tweetId, time = self.tweet_map[user_id][index]
                heapq.heappush(maxheap, [time,tweetId,user_id,index-1])
        return res




    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        
