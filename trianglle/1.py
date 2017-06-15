#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, triangle):
        '''Solution function description'''
        if not triangle: return 0
        n = len(triangle)
        if n == 1: return triangle[0][0]
        for i in range(1, n):
            for j in range(i+1):
                if j == 0: triangle[i][j] += triangle[i-1][j]
                elif j == i: triangle[i][j] += triangle[i-1][j-1]
                else: triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
            print(triangle[i])
        return min(triangle[i])
def main():
    '''main function'''
    _solution = Solution()
    res, inp = [], [[[9],[1,2],[3,0,4]], [[0], [1,2]]]
    for i in inp:
        print('res '+str(_solution.func(i)))

if __name__ == "__main__":
    main()
