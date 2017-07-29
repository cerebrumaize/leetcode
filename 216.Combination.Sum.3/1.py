#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, k, n):
        '''Solution function description'''
        if n > 45 or n < 1: return []
        res = []
        self.helper(res, [], 1, k, n)
        return res
    def helper(self, total_res, part_res, start_ind, k, n):
        '''Solution Helper desciption'''
        if k == 0 and n == 0: total_res.append(part_res)
        if k < 0: return
        if k > 0:
            if n <= 0: return
            for i in range(start_ind, 10):
                self.helper(total_res, part_res+[i], i+1, k-1, n-i)

def main():
    '''main function'''
    _solution = Solution()
    inp = [(3, 15)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
