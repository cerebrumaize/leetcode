#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321
# Given[1,2,3] the total_res is like: [] -> [1] -> [2,1],[1,2] -> [3,2,1][2,3,1][2,1,3], [3,1,2][1,3,2][1,2,3]
class Solution(object):
    '''Solution description'''
    def func(self, nums):
        '''Solution function description'''
        res = [[]]
        for n in nums:
            n_res = []
            for p in res:
                # Insert n at every position
                for i in range(len(p)+1):
                    n_res.append(p[:i] + [n] + p[i:])
            res = n_res
        return res

def main():
    '''main function'''
    _solution = Solution()
    inp = [[1, 2, 3]]
    for i in inp:
        print(sorted(_solution.func(i)))

if __name__ == "__main__":
    main()
