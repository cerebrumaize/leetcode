#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums, target):
        '''Solution function description'''
        from collections import Counter
        s=[t for t in Counter(s).items()]
        s.sort(key=lambda t:t[1], reverse=True)
        res = [k*v for k,v in s]
        return ''.join(res)

def main():
    '''main function'''
    _solution = Solution()
    inp = []
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
