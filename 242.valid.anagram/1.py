#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, s, t):
        '''Solution function description'''
        if len(s) != len(t): return False
        s = sorted(s)
        t = sorted(t)
        return s == t

def main():
    '''main function'''
    _solution = Solution()
    inp = [('anagram', 'nagaram'), ('rat', 'car')]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
