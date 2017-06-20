#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, nums):
        '''Solution function description'''
        if not nums: return 0
        pre_max, pre_min, sav_max, n = nums[0], nums[0], nums[0], len(nums)
        for i in range(1, n):
            cur_max = max(pre_max*nums[i], pre_min*nums[i], nums[i])
            cur_min = min(pre_max*nums[i], pre_min*nums[i], nums[i])
            sav_max = max(cur_max, sav_max)
            pre_max, pre_min = cur_max, cur_min
        return sav_max
def main():
    '''main function'''
    _solution = Solution()
    res, inp = [], [[2,3,-2,4],[-2,3,-2,4],[2,0,3,-2,4],[0,1,3],[2],[-2,0,-8],[2,-5,-2,-4,3]]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
