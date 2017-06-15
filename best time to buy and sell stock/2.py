#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, prices):
        '''Solution function description'''
        curr_max = None
        max_diff = 0
        for i in reversed(prices):
            if curr_max is None or i > curr_max:
                curr_max = i
            curr_diff = curr_max - i
            max_diff = max(max_diff, curr_diff)
        return max_diff

def main():
    '''main function'''
    _solution = Solution()
    res, inp = [], [[7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1]]
    for i in inp:
        res.append(_solution.func(i))
    print(list(res))

if __name__ == "__main__":
    main()
