#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lens = len(nums)
        if not lens:
            return 0

        if lens == 1:
            return nums[0]

        _max = 0
        i = 0
        while i <= lens - 1:
            r = 1
            j = i
            while j <= lens - 1 and nums[j] != 0:
                r = r * nums[j]
                j = j + 1
                if r > _max:
                    _max = r
            i = j + 1

        i = lens-1
        while i >= 0:
            r = 1
            j = i
            while j >= 0 and nums[j] != 0:
                r = r * nums[j]
                j = j - 1
                if r > _max:
                    _max = r
            i = j - 1

        return _max
def main():
    '''main function'''
    _solution = Solution()
    res, inp = [], [[2,3,-2,4],[-2,3,-2,4],[2,0,3,-2,4],[0,1,3],[2],[-2,0,-8],[2,-5,-2,-4,3]]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
