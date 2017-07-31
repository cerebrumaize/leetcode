#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums):
        '''Solution function description'''
        from itertools import combinations
        if len(nums) == 1: return[[], nums]
        res = [[]]
        for i in range(1, len(nums)):
            for t in combinations(nums, i):
                res.append(list(t))
        res.append(nums)
        return res

def main():
    '''main function'''
    _solution = Solution()
    inp = [[0]]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
