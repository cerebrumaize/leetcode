#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103
class TreeNode(object):
    '''Solution description'''
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    '''Solution description'''
    def generateTrees(self, n):
        '''Solution function description'''
        if not n: return []
        d = {}
        def helper(first, last):
            if (first, last) in d: return d[(first, last)]
            if first > last: return [None]
            res = []
            for v in range(first, last+1):
                for l in helper(first, v-1):
                    for r in helper(v+1, last):
                        root = TreeNode(v)
                        root.left = l
                        root.right = r
                        res.append(root)
            d[(first, last)] = res
            return res
        return helper(1, n)
def main():
    '''main function'''
    _solution = Solution()
    res, in_params = [], [0, 1, 2, 3]
    for i in in_params:
        print(i)
        res.append(_solution.generateTrees(i))
    print(list(res))

if __name__ == "__main__":
    main()
