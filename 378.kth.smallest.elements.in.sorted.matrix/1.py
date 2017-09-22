#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, matrix, k):
        '''Solution function description'''
        m = len(matrix)
        n = len(matrix[0])
        tags = [[False] * n for _ in range(m)]
        res = [(matrix[0][0], 0, 0)]
        count = 0
        tags[0][0] = True
        from heapq import heappop, heappush
        while res and count <= k:
            v, i, j = heappop(res)
            count += 1
            if count==k: return v
            else:
                if i+1<m and not tags[i+1][j]:
                    heappush(res, (matrix[i+1][j], i+1, j))
                    tags[i+1][j] = True
                if j+1<n and not tags[i][j+1]:
                    heappush(res, (matrix[i][j+1], i, j+1))
                    tags[i][j+1] = True

def main():
    '''main function'''
    _solution = Solution()
    inp = [([[1,3,5],[6,7,12],[11,14,14]], 6)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
