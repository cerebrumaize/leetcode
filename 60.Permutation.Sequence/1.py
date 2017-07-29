#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, n, k):
        '''Solution function description'''
        if k == 1: return list(range(1, n+1))
        res = []
        list_k = [k]
        self.helper(res, list(range(1, n+1)), list_k, n)
        return res
    def helper(self, cur_res, options, k, n):
        '''Solution helper description'''
        if not options:
            k[0] -= 1
            if k[0] == 0: return
            cur_res = []
        for i, e in enumerate(options):
            if k[0] > 0:
                self.helper(cur_res+[e], options[:i]+options[i+1:], k, n)

def main():
    '''main function'''
    _solution = Solution()
    inp = [(3, 4)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
