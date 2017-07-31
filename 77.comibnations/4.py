#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, n, k):
        '''Solution function description'''
        res = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k: res.append(stack[:])
            if l == k or n-x+1 < k-l:
                if not stack: return res
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1

def main():
    '''main function'''
    _solution = Solution()
    inp = [(3, 3), (4, 3)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
