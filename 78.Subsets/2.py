#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums):
        '''Solution function description'''
        if not nums: return [[]]
        res = []
        self.helper(res, [], nums)
        return res

    def helper(self, total, part, nums):
        '''Solution function description'''
        total.append(part)
        if len(nums) == 1:
            total.append(part+[nums[0]])
            return
        for i, e in enumerate(nums):
            self.helper(total, part+[e], nums[i+1:])

def main():
    '''main function'''
    _solution = Solution()
    inp = [[], [0], [3,2,4]]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
