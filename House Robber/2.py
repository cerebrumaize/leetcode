#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-2]+nums[i], nums[i-1])
        return max(nums[-1], nums[-2])

def main():
    '''main function'''
    _solution = Solution()
    res, inp = [], [[1,1,2,1],[16,1,1,8,1,1,9],[2,1,1,2], [0], [0,2], [3,1],[4,8,2,1,9],[4,2,3,1,9]]
    for i in inp:
        print(_solution.rob(i))

if __name__ == "__main__":
    main()
