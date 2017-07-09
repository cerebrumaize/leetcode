#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not g or not s: return 0
        g, s = sorted(g), sorted(s)
        if s[-1] < g[0]: return 0
        gi, si, res = 0, 0, 0
        while gi < len(g) and si < len(s):
            if g[gi] <= s[si]:
                res += 1
                gi += 1
                si += 1
            elif g[gi] > s[si]:
                si += 1
        return res

def main():
    '''main function'''
    _solution = Solution()
    inp = [([1, 1, 1], [1, 2, 3]), ([5, 1], [1, 2, 3])]
    for i in inp:
        print(_solution.findContentChildren(i[0], i[1]))

if __name__ == "__main__":
    main()
