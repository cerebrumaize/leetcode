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
        if n == 0:return []
        self.memory = [[[] for _ in range(n+1)] for _ in range(n+1)]
        return self.build_trees(1, n)
    def build_trees(self, first, last):
        '''Solution function description'''
        if first < last:return [None]
        if first == last:return [TreeNode(first)]
        if self.memory[first][last]:return self.memory[first][last]
        for v in range(first, last+1):
            left = self.build_trees(first, v-1)
            right = self.build_trees(v+1, last)
            for l in left:
                for r in right:
                    root = TreeNode(v)
                    self.memory[first][last].append(root)
                    root.left = l
                    root.right = r
        return self.memory[first][last]
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
