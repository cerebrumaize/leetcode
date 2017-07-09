#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, nums, S):
        '''Solution function description'''
        if not nums: return 0
        d = {nums[0]:1, -nums[0]:1} if nums[0] != 0 else {0:2}
        for i in range(1, len(nums)):
            tmpd = {}
            for k in d:
                tmpd[k+nums[i]] = tmpd.get(k+nums[i], 0)+d.get(k, 0)
                tmpd[k-nums[i]] = tmpd.get(k-nums[i], 0)+d.get(k, 0)
            print(tmpd)
            d = tmpd
        return d.get(S, 0)
def main():
    '''main function'''
    _solution = Solution()
    inp = [([1, 1, 1, 1, 1], 3)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
