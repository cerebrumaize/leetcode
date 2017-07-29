#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, N):
        '''Solution function description'''
        if N == 0: return []
        if N == 1: return [1]
        if N == 2: return [[1, 2], [2, 1]]
        res = []
        self.helper(res, [], list(range(1, N+1)), N)
        return res
    def helper(self, total_res, part_res, options, N):
        '''Solution helper description'''
        if len(part_res) == N:
            total_res.append(part_res)
        for i, e, in enumerate(options):
            if (len(part_res)+1)%e == 0 or e%(len(part_res)+1) == 0:
                self.helper(total_res, part_res+[e], options[:i]+options[i+1:], N)

def main():
    '''main function'''
    _solution = Solution()
    inp = [3]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
