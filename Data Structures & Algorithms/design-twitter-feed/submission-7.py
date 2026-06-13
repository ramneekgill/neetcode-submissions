class Twitter:

    def __init__(self):
        self.tweets = []
        self.follows = {}
        

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append([userId, tweetId])

        

    def getNewsFeed(self, userId: int) -> List[int]:
        size = 0
        ls = []
        for i in range(len(self.tweets)-1, -1, -1):
            if (userId in self.follows and self.tweets[i][0] in self.follows[userId]) or self.tweets[i][0] == userId:
                ls.append(self.tweets[i][1])
                size += 1
            if size == 10:
                break
        return ls

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows or followeeId not in self.follows[followerId]:
            return
        self.follows[followerId].remove(followeeId)
        
        
