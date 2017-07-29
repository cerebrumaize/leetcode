#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums):
        '''Solution function description'''
        res = []
        if not nums: return res
        self.helper(res, [], nums)
        return res
    def helper(self, total_res, part_res, options):
        '''Solution function description'''
        if options:
            for i, e in enumerate(options):
                self.helper(total_res, part_res+[e], options[0:i]+options[i+1:])
        else: total_res.append(part_res)

def main():
    '''main function'''
    _solution = Solution()
    inp = [[1, 2, 3]]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
