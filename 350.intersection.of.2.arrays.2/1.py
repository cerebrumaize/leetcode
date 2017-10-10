#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums1, nums2):
        '''Solution function description'''
        d = {}
        for e in nums1:
            if e not in d: d[e] = [1, 0]
            else: d[e][0] += 1

        for e in nums2:
            if e not in d: d[e] = [0, 1]
            else: d[e][1] += 1

        res = []
        for k, v in d.items():
            c = min(v)
            if c == 0: continue
            else:
                res += [k]*c

def main():
    '''main function'''
    _solution = Solution()
    inp = [([1,2,1,2], [2,2]), ([], [1])]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
