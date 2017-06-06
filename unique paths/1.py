
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, m, n):
        '''
        Solution function description
        '''
        #res = [[1]*n]*m
        res = [[1] * n for i in range(m)]
        for i in xrange(1, m):
            for j in xrange(1, n):
                res[i][j] = res[i-1][j] + res[i][j-1]
                print res[i][j], i, j
        print res[0], res[1], res[2]
        return res[m-1][n-1]

def main():
    '''main function'''
    _solution = Solution()
    res = _solution.func(3, 4)
    print res

if __name__ == "__main__":
    main()
