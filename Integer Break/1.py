#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, n):
        '''Solution function description'''
        if n == 2: return 1
        if n == 3: return 2
        m, n = divmod(n, 3)
        if n == 0: return pow(3, m)
        elif n == 1: return pow(3, m-1)*4
        else: return pow(3, m)*n

def main():
    '''main function'''
    _solution = Solution()
    inp = [2, 10]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
