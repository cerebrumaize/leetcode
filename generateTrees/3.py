#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103
class Solution(object):
    '''Solution description'''
    def generateTrees(self, n):
        """
        catalan number:https://zh.wikipedia.org/wiki/%E5%8D%A1%E5%A1%94%E5%85%B0%E6%95%B0
        :type n: int
        :rtype: int
        """
        from functools import reduce
        nums = reduce(lambda x, y: x*y, range(n+2, 2*n+1), 1)
        return reduce(lambda x, y: x/y, range(1, n+1), nums)
def main():
    '''main function'''
    _solution = Solution()
    in_param = [0, 1, 2, 3, 4, 5, 6]
    for i in in_param:
        res = _solution.generateTrees(i)
        print(res)

if __name__ == "__main__":
    main()
