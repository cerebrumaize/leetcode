#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def helper(self, total, part, options, k):
        '''Solution function description'''
        if k == 0:
            total.append(part)
            return
        for i, e in enumerate(options):
            self.helper(total, part+[e], options[i+1:], k-1)

    def func(self, n, k):
        '''Solution function description'''
        res = []
        if k == 0: return [[]]
        self.helper(res, [], list(range(1, n+1)), k)
        return res

def main():
    '''main function'''
    _solution = Solution()
    inp = [(4, 2)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
