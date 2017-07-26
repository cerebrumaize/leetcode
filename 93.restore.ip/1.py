#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, s):
        '''Solution function description'''
        ans = []
        self.helper(s, 4, '', ans, len(s))
        return ans
    def helper(self, s, n, result, results, stdlen):
        '''Solution function description'''
        if len(s) < n or len(s) > 3*n: return
        if n == 0:
            #below restriction makes sure that no 010 to 10 to store in final result
            if len(result[1:])-3 == stdlen:
                results.append(result[1:])
            return
        for i in range(min(3, len(s))):
            if int(s[:(i+1)]) < 256:
                self.helper(s[(i+1):], n-1, result+"."+s[:(i+1)], results, stdlen)
        return

def main():
    '''main function'''
    _solution = Solution()
    inp = ['010010']
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
