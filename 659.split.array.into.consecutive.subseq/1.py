#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums):
        '''Solution function description'''
        if len(nums) < 3: return False
        prev = nums[0]-1
        count = 0
        for i, e in enumerate(nums):
            if e != prev+1:
                if count < 3: return False
                count = 1
            else:
                count += 1
            prev = e
        if count < 3: return False
        return True

def main():
    '''main function'''
    _solution = Solution()
    inp = [[1,2,3,3,4,4,5,5], [1,2,3,3,4,5], [1,2,3,4,4,5]]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
