#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums):
        '''counting sort'''
        l = list(range(len(nums)))
        for n in nums:
            l[n-1] += 1
        for i in range(len(1, l)):
            l[i] += l[i-1]
        res = list(range(len(nums)))
        for i in range(len(nums)):
            res[l[nums[i]-1]] = nums[i]
            l[nums[i]] -= 1
        return res

def main():
    '''main function'''
    _solution = Solution()
    inp = [[1, 4, 1, 2, 7, 5, 2]]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
