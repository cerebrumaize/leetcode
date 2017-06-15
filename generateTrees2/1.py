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
        def node(val, l, r):
            '''Solution function description'''
            n = TreeNode(val)
            n.left = l
            n.right = r
            return n
        def trees(first, last):
            '''Solution function description'''
            return [node(root, left, right)
                    for root in range(first, last+1)
                    for left in trees(first, root-1)
                    for right in trees(root+1, last)] or [None]
        return trees(1, n)
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
