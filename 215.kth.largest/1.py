#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums, k):
        '''Solution function description'''
        if len(nums) == 1: return nums[0]
        pivot = nums[0]
        l, m, r = [], [], []
        for i in nums:
            if i < pivot: r.append(i)
            elif i == pivot: m.append(i)
            else: l.append(i)
        if len(l) >= k: return self.func(l, k)
        elif len(l) + len(m) >= k: return m[-1]
        else: return self.func(r, k-len(l)-len(m))

def main():
    '''main function'''
    _solution = Solution()
    inp = [([7,6,5,4,3,2,1], 2)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
