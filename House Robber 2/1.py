#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def helper(self, nums):
        """type nums: List[int]
        :rtype: int"""
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-2]+nums[i], nums[i-1])
        return max(nums[-1], nums[-2])
    def rob(self, nums):
        '''Solution function description'''
        if not nums: return 0
        if len(nums) == 1: return nums[-1]
        if len(nums) == 2: return max(nums)
        res1 = nums[0] + self.helper(nums[2:-1])
        res2 = self.helper(nums[1:])
        return max(res1, res2)

def main():
    '''main function'''
    _solution = Solution()
    inp = [[1,2,1,1]]
    for i in inp:
        print(_solution.rob(i))

if __name__ == "__main__":
    main()
