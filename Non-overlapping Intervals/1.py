#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, intervals):
        '''Solution function description'''
        intervals.sort(key=lambda x: (x[1]))
        right = intervals[0][0]-1
        print(intervals)
        res = 0
        for i in intervals:
            if i[0] < right: res += 1
            else: right = i[1]
        return res

def main():
    '''main function'''
    _solution = Solution()
    inp = [[[1,2], [2,3], [3,4], [1,3]], [[1,2], [1,2], [1,2]], [[1,2], [2,3]], \
           [[1,2],[1,3],[1,4]], [[1,100],[11,22],[1,11],[2,12]], [[0,2],[1,3],[2,4],[3,5],[4,6]]]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
