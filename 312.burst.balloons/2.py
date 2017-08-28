#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, iNums):
        '''func description'''
        nums = [1] + [i for i in iNums if i > 0] + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]

        for k in range(2, n):
            for l in range(0, n - k):
                r = l + k
                for i in range(l+1, r):
                    dp[l][r] = max(dp[l][r], nums[l]*nums[i]*nums[r]+dp[l][i]+dp[i][r])
        return dp[0][n - 1]

def main():
    '''main function'''
    _solution = Solution()
    inp = [[3, 1, 5, 8]]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
