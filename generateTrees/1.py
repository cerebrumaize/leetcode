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
        def node(val, left, right):
            '''Solution function description'''
            n = TreeNode(val)
            n.left = left
            n.right = right
            return n
        def trees(first, last):
            if n==0: return []
            res = []
            for root in range(first, last+1):
                for left in trees(first, root-1):
                    for right in trees(root+1, last):
                        res.append(node(root, left, right))
            return res or [None]

        return len(trees(1, n))


def main():
    '''main function'''
    _solution = Solution()
    in_param = [0, 1, 2, 3, 4, 5, 6]
    for i in in_param:
        res = _solution.generateTrees(i)
        print(res)

if __name__ == "__main__":
    main()
