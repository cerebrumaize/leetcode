#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def majorityElement(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        a = self.majorityElement(nums[:len(nums)//2])
        b = self.majorityElement(nums[len(nums)//2:])
        if a == b:
            return a
        return [b, a][nums.count(a) > len(nums)//2]


def main():
    '''main function'''
    _solution = Solution()
    inp = [[1], [2,1,2,3,4,3,2]]
    for i in inp:
        print(_solution.majorityElement(i))

if __name__ == "__main__":
    main()
