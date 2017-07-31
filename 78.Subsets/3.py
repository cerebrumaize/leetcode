#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums):
        '''Solution function description'''
        res = [[]]
        for n in nums:
            res += [item + [n] for item in res]
        return res

def main():
    '''main function'''
    _solution = Solution()
    inp = [[], [3], [5,2,1]]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
