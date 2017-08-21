#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums, k):
        '''Solution function description'''
        if not nums: return 0
        res = 0
        n = len(nums)
        for i in range(n):
            tmpsum=0
            for j in range(i,n):
                tmpsum += nums[j]
                if tmpsum == k:
                    res+=1
        return res

def main():
    '''main function'''
    _solution = Solution()
    inp = [([1,1,1],2), ([2,3,2,3,2],5), ([28,54,7,-70,22,65,-6], 100),([0,0,0,0,0,0,0,0,0,0],0)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
