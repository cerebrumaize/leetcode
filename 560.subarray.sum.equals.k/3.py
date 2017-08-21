#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums, k):
        '''Solution function description'''
        if not nums: return 0
        total, res, d = 0, 0, {0:1}
        for i in nums:
            total += i
            res += d.get(total-k, 0)
            if total in d: d[total] += 1
            else: d[total] = 1
        return res

def main():
    '''main function'''
    _solution = Solution()
    inp = [([1,1,1],2), ([2,3,2,3,2],5), ([28,54,7,-70,22,65,-6], 100),([0,0,0,0,0,0,0,0,0,0],0)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
