#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, s, t):
        '''Solution function description'''
        if not s and not t: return True
        if len(s) != len(t): return False

        for i in set(s.lowercase()):
            if s.count(i) != t.count(i): return False

        return True

def main():
    '''main function'''
    _solution = Solution()
    inp = []
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
