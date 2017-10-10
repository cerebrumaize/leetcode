#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321
import collections
import heapq
class Twitter(object):

    def __init__(self):
        self.tweets = collections.defaultdict(list)
        self.follows = collections.defaultdict(set)
        self.time = -1

    def postTweet(self, userId, tweetId):
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId):
        all_users = []
        if userId in self.tweets:
            all_users.append(userId)

        if userId in self.follows:
            all_users += self.follows[userId]

        heap = []
        for uid in all_users:
            if uid in self.tweets:
                heap.append((self.tweets[uid][-1], uid, len(self.tweets[uid])-1))

        heapq.heapify(heap)
        res, count = [], 10
        while count > 0:
            if not heap: break

            tweet, uid, idx = heapq.heappop(heap)
            _, tweetId = tweet
            res.append(tweetId)
            count -= 1

            if idx > 0:
                heapq.heappush(heap, (self.tweets[uid][idx-1], uid, idx-1))

        return res


    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

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
