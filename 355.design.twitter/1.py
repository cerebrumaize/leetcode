#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321
import collections
class Twitter(object):
    '''simple twitter emulator'''
    def __init__(self):
        '''
        initialize data structure here
        '''
        self.user_tweets = collections.deque()
        #(userid, tweetid)
        self.follow_info = {}
        #follower: [followee1, followee2 ...]

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.user_tweets.appendleft((userId, tweetId))
        if userId not in self.follow_info:
            self.follow_info[userId] = []


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. 
        Each item in the news feed must be posted by users who the user followed or by the user herself. 
        Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId in self.follow_info:
            followees = self.follow_info[userId] + [userId]
        else:
            followees = [userId]
        i, res = 0, []
        while i < len(self.user_tweets) and len(res) < 10:
            if self.user_tweets[i][0] in followees:
                res.append(self.user_tweets[i][1])
            i += 1
        return res

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.follow_info:
            self.follow_info[followerId] = []
        if followeeId in self.follow_info[followerId]:
            return
        else:
            self.follow_info[followerId].append(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.follow_info or followeeId not in self.follow_info[followerId]:
            return
        else:
            self.follow_info[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

class Solution(object):
    '''Solution description'''
    def func(self, nums, target):
        '''Solution function description'''

def main():
    '''main function'''
    _solution = Solution()
    inp = []
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
