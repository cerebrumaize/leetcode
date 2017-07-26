#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, n):
        '''Solution function description'''
        tmp = []
        def total(x):
            for _ in range(2*x): tmp.append(['(', ')'])
            from itertools import product
            for i in product(*tmp):
                yield i
        res = []
        for s in total(n):
            #print(s)
            counter = i = 0
            while i < 2*n:
                if s[i] == '(': counter += 1
                else: counter -= 1
                if counter < 0 or counter > n: break
                i += 1
            if counter == 0 and i == 2*n: res.append(s)
        return res
def main():
    '''main function'''
    _solution = Solution()
    inp = [2, 3, 9, 0]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
