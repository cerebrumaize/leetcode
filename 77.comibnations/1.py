#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321
from itertools import combinations
class Solution(object):
    '''Solution description'''
    def func(self, n, k):
        '''Class Solution function'''
        return list(combinations(range(1, n+1), k))

def main():
    '''main function'''
    _solution = Solution()
    inp = [(3, 3), (4, 3)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
