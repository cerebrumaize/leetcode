#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def helper(self, s, counter, n, res):
        '''helper func'''
        if counter < 0: return
        if len(s) == 2*n:
            if counter == 0: res.append(s)
            return
        self.helper(s+'(', counter+1, n, res)
        self.helper(s+')', counter-1, n, res)
    def func(self, n):
        '''Solution function description'''
        res = []
        self.helper('', 0, n, res)
        return res
def main():
    '''main function'''
    _solution = Solution()
    inp = [2, 3, 0]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
