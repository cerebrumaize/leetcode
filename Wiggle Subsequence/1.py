#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, nums):
        '''Solution function description'''
        if not nums: return 0
        if len(nums) == 1: return 1
        if len(nums) == 2: return 1 if nums[0] == nums[-1] else 2
        tmp = [nums[i]-nums[i-1] for i in range(1, len(nums))]
        prev = tmp[0]
        cur_len = 1
        for i in range(1, len(tmp)):
            if tmp[i]*prev < 0:
                cur_len += 1
            if tmp[i] != 0:
                prev = tmp[i]
        return cur_len if prev == 0 else cur_len + 1

def main():
    '''main function'''
    _solution = Solution()
    inp = [[1, 1], [1, 2], [1], [], [1, 17, 5, 10, 13, 15, 10, 5, 16, 8],\
           [2, 2, 3, 3], [2, 2, 2, 3], [0, 0, 0], [0, 4, 6], [0, 2, -2, 2, -2]]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
