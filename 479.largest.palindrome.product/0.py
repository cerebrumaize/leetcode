#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def largestPalindrome(self, n):
        if n==1: return 9
        if n==2: return 987
        for a in range(2, 9*10**(n-1)):
            hi=(10**n)-a
            lo=int(str(hi)[::-1])
            if a**2-4*lo < 0: continue
            if (a**2-4*lo)**.5 == int((a**2-4*lo)**.5):
                return (lo+10**n*(10**n-a))%1337


def main():
    '''main function'''
    _solution = Solution()
    inp = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in inp:
        print(_solution.largestPalindrome(i))

if __name__ == "__main__":
    main()
