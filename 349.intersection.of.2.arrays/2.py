#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums1, nums2):
        '''Solution function description'''
        s1 = set(nums1)
        s2 = set(nums2)

        return s1.intersection(s2)

def main():
    '''main function'''
    _solution = Solution()
    inp = [([1,2,1,2], [2,2]), ([], [1]), ([1,2,1,2], [2])]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
