#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, prices):
        '''Solution function description'''
        if not prices or len(prices) <= 1: return 0
        result = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                result += (prices[i]-prices[i-1])
        return result

def main():
    '''main function'''
    _solution = Solution()
    inp = [[1,7,8,5],[7,1,8,5],[5],[],[1,7,7],[8,7,7,7]]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
