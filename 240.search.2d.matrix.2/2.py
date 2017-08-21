#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, matrix, target):
        '''Solution function description'''
        n_rows = len(matrix)
        if n_rows == 0: return False
        n_col = len(matrix[0])
        i, j = 0, n_col-1
        while j >= 0 and i < n_rows:
            if matrix[i][j] == target: return True
            elif matrix[i][j] > target: j -= 1
            else: i += 1

def main():
    '''main function'''
    _solution = Solution()
    inp = [([[-1, 2], [1, 3]], 2)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
