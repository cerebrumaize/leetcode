#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums):
        '''Solution function description'''
        if not nums: return None
        if len(nums) == 1: return nums[0]
        count, res = 1, nums[0]
        for i in nums[1:]:
            if i == res: count += 1
            else: count -= 1
            if count < 0:
                res = i
                count = 0
        return res


def main():
    '''main function'''
    _solution = Solution()
    inp = [[1]]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
