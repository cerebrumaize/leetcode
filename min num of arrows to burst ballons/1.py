#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, points):
        '''Solution function description'''
        if not points: return 0
        points.sort(key=lambda x: x[1])
        x2, res = points[0][0]-1, 0
        for b in points:
                x2 = b[1]
                res += 1
        return res

def main():
    '''main function'''
    _solution = Solution()
    inp = [[[10,16], [2,8], [1,6], [7,12]]]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
