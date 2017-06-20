#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103
class TreeLinkNode:
    '''Definition for binary tree with next pointer.'''
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution(object):
    '''Solution description'''
    def connect(self, root):
        '''Solution function description'''
        while root and root.left:
            next_layer = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next_layer

def main():
    '''main function'''
    _solution = Solution()
    res, inp = [], []
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
