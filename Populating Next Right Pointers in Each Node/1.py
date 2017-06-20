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
    def helper(self, l):
        res = []
        for i in range(len(l)):
            if i < len(l)-1: l[i].next = l[i+1]
            else: l[i].next = None
            res.append(l[i].left)
            res.append(l[i].right)
        return res

    def connect(self, root):
        '''Solution function description'''
        if not root: return
        sav_layer = [root]
        while sav_layer[0].left:
            sav_layer = self.helper(sav_layer)
        for i in range(len(sav_layer)):
            if i < len(sav_layer)-1: sav_layer[i].next = sav_layer[i+1]
            else: sav_layer[i].next = None

def main():
    '''main function'''
    _solution = Solution()
    res, inp = [], []
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
