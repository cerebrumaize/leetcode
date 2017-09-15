#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums, k):
        '''Solution function description'''
        from collections import Counter
        nums_count = Counter(nums)
        from heapq import nlargest
        return nlargest(k, nums_count, key=lambda x: nums_count[x])

def main():
    '''main function'''
    _solution = Solution()
    inp = [([1,2,2,2,1,1,3],2)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
