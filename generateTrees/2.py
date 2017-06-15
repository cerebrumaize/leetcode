#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103
class Solution(object):
    '''Solution description'''
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: int
        G(n), F(i, n)
        """
        if not n: return 0
        if n == 1: return 1
        res = [0] * (n+1)
        res[0] = res[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                res[i] += res[j-1]*res[i-j]
        print(res)
        return res[n]

def main():
    '''main function'''
    _solution = Solution()
    in_param = [0, 1, 2, 3, 4, 5, 6]
    for i in in_param:
        res = _solution.generateTrees(i)
        print(res)

if __name__ == "__main__":
    main()
