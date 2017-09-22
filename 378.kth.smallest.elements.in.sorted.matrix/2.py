#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, matrix, k):
        '''Solution function description'''
        low, high = matrix[0][0], matrix[-1][-1]
        while low<high:
            mid = low + (high - low)/2
            count, j = 0, len(matrix[0])-1
            for i in range(len(matrix)):
                while j>=0 and matrix[i][j] > mid:
                    j -= 1
                count += (j+1)
            if count < k: low = mid+1
            else: high = mid
        return low
        
def main():
    '''main function'''
    _solution = Solution()
    inp = [([[1,3,5],[6,7,12],[11,14,14]], 6)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
