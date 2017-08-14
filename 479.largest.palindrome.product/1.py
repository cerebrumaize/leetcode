#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def notPalindrome(self, x):
        s = str(x)
        l = len(s)
        return s[:l//2]!=s[:l//2-1:-1]
    def helper(self, n):
        if n==1: return
        for i in range(n):
            for j in range(9, -1, -1):
                return str(j)+self.helper(i-1)
    def func(self, n):
        '''Solution function description'''
        if n==1: return 9
        if n==2: return 987
        lo, high=int('1'+'0'*(n-1)), int('9'*n)
        step = lo
        divisor = high
        for i in range(high*high, lo*lo-1, -1):
            if self.notPalindrome(i): continue
            for tmp_div in range(divisor, step-1, -1):
                if i%tmp_div == 0:
                    if len(str(i//tmp_div)) == n:
                        print(i, i//tmp_div, tmp_div)
                        return i%1337
                    elif len(str(i//tmp_div)) > n: break

def main():
    '''main function'''
    _solution = Solution()
    inp = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
