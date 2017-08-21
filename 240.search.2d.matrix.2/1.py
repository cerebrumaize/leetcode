#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, matrix, target):
        '''Solution function description'''
        if not matrix: return False
        if len(matrix) == 1: return target in matrix[0]
        if len(matrix[0]) == 1: return target in list(matrix[i][0] for i in range(len(matrix)))
        up = left = 0
        down = len(matrix)-1
        right = len(matrix[0])-1
        for i in range(len(matrix)):
            if target > matrix[i][-1]: continue
            elif matrix[i][0] <= target <= matrix[i][-1]:
                up = i
                break
        for i in range(1, len(matrix)+1):
            if target < matrix[-i][0]: continue
            else:
                down = len(matrix)-i
                break
        for i in range(len(matrix[0])):
            if matrix[-1][i] > target: continue
            else:
                left = i
                break
        for i in range(1, len(matrix[0])+1):
            if matrix[0][-i] > target: continue
            else:
                right = len(matrix[0])-i
                break

        for i in range(up, down+1):
            for j in range(left, right+1):
                if matrix[i][j] == target: return True
                if matrix[i][j] > target: break
            return False

def main():
    '''main function'''
    _solution = Solution()
    inp = [([[1,4],[2,5]], 5)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
