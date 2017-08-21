#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def longestIncrasingPath(self, matrix):
        '''Solution function description'''
        row = len(matrix)
        col = len(matrix[0])
        mem = [[0]*col for _ in range(row)]
        def dfs(i,j):
            res=1
            if not mem[i][j]:
                if i and matrix[i-1][j] > matrix[i][j]:
                    res=max(res, 1+dfs(i-1,j))
                if i<row-1 and matrix[i+1][j]>matrix[i][j]:
                    res=max(res, 1+dfs(i+1,j))
                if j and matrix[i][j-1]>matrix[i][j]:
                    res =max(res, 1+dfs(i,j-1))
                if j<col-1 and matrix[i][j+1]>matrix[i][j]:
                    res=max(res, 1+dfs(i,j+1))
                mem[i][j] = res
            return mem[i][j]
        return max(dfs(x,y) for x in range(row) for y in range(col))


def main():
    '''main function'''
    _solution = Solution()
    inp = [ [[9,9,4],[6,6,8],[2,1,1]], [[3,4,5],[3,2,6],[2,2,1]] ]
    for i in inp:
        print(_solution.longestIncrasingPath(i))

if __name__ == "__main__":
    main()
