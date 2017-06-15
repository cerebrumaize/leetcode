#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, prices):
        '''Solution function description'''
        if not prices: return 0
        minimum = prices[0]
        for i in range(len(prices)):
            minimum = min(minimum, prices[i])
            prices[i] -= minimum
        print(prices)
        return max(prices)

def main():
    '''main function'''
    _solution = Solution()
    res, inp = [], [[7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1]]
    for i in inp:
        res.append(_solution.func(i))
    print(list(res))

if __name__ == "__main__":
    main()
