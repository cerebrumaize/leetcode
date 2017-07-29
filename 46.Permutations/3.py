#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def permute(self, nums):
        '''Solution function description'''
        if not nums: return []
        if len(nums) == 1: return [nums]
        r = []
        for a in self.permute(nums[1:]):
            for j in range(len(a)+1):
                r.append(a[:j] + [nums[0]] + a[j:])
        return r  

def main():
    '''main function'''
    _solution = Solution()
    inp = [[1, 1, 2, 3]]
    for i in inp:
        print(sorted(_solution.permute(i)))

if __name__ == "__main__":
    main()
