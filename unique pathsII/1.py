
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, obstacleGrid):
        '''
        Solution function description
        '''
        og = obstacleGrid
        if not og: return 0
        og[0][0] = not og[0][0]
        m, n = len(og), len(og[0])
        for i in xrange(1, m):
            og[i][0] = (not og[i][0]) & og[i-1][0]
        for j in xrange(1, n):
            og[0][n] = (not og[0][n]) & og[0][j-1]
        for i in xrange(1, m):
            for j in xrange(1, n):
                if og[i][j] == 1:
                    og[i][j] = 0
                else:
                    og[i][j] = og[i-1][j] + og[i][j-1]
        return og[m-1][n-1]

def main():
    '''main function'''
    _solution = Solution()
    a = [[0, 0, 0], [1, 0, 0]]
    res = _solution.func(a)
    print res

if __name__ == "__main__":
    main()
