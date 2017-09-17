#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums1, nums2, k):
        '''Solution function description'''
        from heapq import nsmallest
        from itertools import product
        return list(map(list, nsmallest(k, product(nums1, nums2), key=sum)))
        #return nsmallest(k, ([u, v] for u in nums1 for v in nums2), key=sum)

def main():
    '''main function'''
    _solution = Solution()
    inp = [([1,1,2], [1,2,3], 2)]
    for i in inp:
        print(_solution.func(i[0], i[1], i[2]))

if __name__ == "__main__":
    main()
