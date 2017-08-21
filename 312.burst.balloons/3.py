#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def maxCoins(self, nums):
        '''Solution function description'''
        nums=[1]+nums+[1]
        n=len(nums)
        ans=[[0]*n for _ in range(n)]

        for interval in range(2,n):
            for start in range(n-interval):
                end=start+interval
                ans[start][end]=max([nums[start]*nums[mid]*nums[end]+ans[start][mid]+ans[mid][end] for mid in range(start+1,end)])
        return ans[0][n-1]

def main():
    '''main function'''
    _solution = Solution()
    inp = [[3,1,5,8]]
    for i in inp:
        print(_solution.maxCoins(i))

if __name__ == "__main__":
    main()
