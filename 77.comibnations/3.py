#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, n, k):
        '''Solution function description'''
        if k == 0: return [[]]
        if k == 1: return list([i] for i in range(1, n+1))
        total = []
        for i in range(1, n+1):
            for pre in self.func(i-1, k-1):
                total.append(pre+[i])
        return total

def main():
    '''main function'''
    _solution = Solution()
    inp = [(3, 3), (4, 3)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
