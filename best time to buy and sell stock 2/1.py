#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, prices):
        '''Solution function description'''
        res, holding = 0, False
        if len(prices) <= 1: return 0
        for i in range(len(prices[:-1])):
            if prices[i] < prices[i+1] and not holding:
                res += -prices[i]
                holding = True
            elif prices[i] > prices[i+1] and holding:
                res += prices[i]
                holding = False
            else:
                res += 0
        return (res+prices[-1]) if holding else res

def main():
    '''main function'''
    _solution = Solution()
    inp = [[1,7,8,5],[7,1,8,5],[5],[],[1,7,7],[8,7,7,7]]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
