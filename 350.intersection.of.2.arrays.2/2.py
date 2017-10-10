#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums1, nums2):
        '''Solution function description'''
        d = {}
        res = []
        for e in nums1:
            d[e] = d.get(e, 0) + 1
        for e in nums2:
            if e in d and d[e] > 0:
                res += [e]
                d[e] -= 1
        return res

def main():
    '''main function'''
    _solution = Solution()
    inp = [([1,2,1,2], [2,2]), ([], [1]), ([1,2,1,2], [2])]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
