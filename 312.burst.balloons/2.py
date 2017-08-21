#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def maxCoins(self, nums):
        '''Solution function description'''
        mid = [1]+nums+[1]
        n = len(mid)
        dp = [[0] * n for _ in range(n)]
        for k in range(2, n):
            for left in range(n-k):
                right = left + k
                for i in range(left+1, right):
                    dp[left][right] = max(dp[left][right],\
                                          mid[left]*mid[i]*mid[right]+dp[left][i]+dp[i][right])
        return dp[0][n-1]

def main():
    '''main function'''
    _solution = Solution()
    inp = [[3,1,5,8]]
    for i in inp:
        print(_solution.maxCoins(i))

if __name__ == "__main__":
    main()
