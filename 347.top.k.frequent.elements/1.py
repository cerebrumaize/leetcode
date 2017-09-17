#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums, k):
        '''Solution function description'''
        from collections import Counter
        nums = Counter(nums)
        res = nums.most_common(k)
        return [x[0] for x in res]

def main():
    '''main function'''
    _solution = Solution()
    inp = [([1,1,2,1,4,5,2,2,2,2], 2)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
