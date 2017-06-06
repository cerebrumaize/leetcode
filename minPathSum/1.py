
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, grid):
        '''
        Solution function description
        '''
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        res = [[0] * n for i in xrange(m)]
        res[0][0] = grid[0][0]
        for i in xrange(1, m):
            res[i][0] = res[i-1][0]+grid[i][0]
        for j in xrange(1, n):
            res[0][j] = res[0][j-1]+grid[0][j]
        for i in xrange(1, m):
            for j in xrange(1, n):
                res[i][j] = min(res[i-1][j]+grid[i][j], res[i][j-1]+grid[i][j])
        print res
        return res[-1][-1]

def main():
    '''main function'''
    _solution = Solution()
    a = [[1, 2, 4], [3, 4, 0], [1, 1, 1]]
    res = _solution.func(a)
    print res

if __name__ == "__main__":
    main()
