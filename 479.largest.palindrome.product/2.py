#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def helper(self, n, k, part, total):
        if k==0:
            total.append(part)
            return
        for i in range(9, -1 if k<n else 0, -1):
            self.helper(n, k-1, part+str(i), total)

    def largestPalindrome(self, n):
        if n==1: return 9
        if n==2: return 987
        res = []
        self.helper(n, n, '', res)
        lo, high=int('1'+'0'*(n-1)), int('9'*n)
        for i in res:
            t = int(i+i[::-1])
            for tmp_div in range(high, lo-1, -1):
                if t > tmp_div**2: break
                if t < lo**2-1: break
                d, m = divmod(t, tmp_div)
                if len(str(d)) > len(str(tmp_div)): break
                if m == 0 and len(str(d)) == len(str(tmp_div)): return t%1337

def main():
    '''main function'''
    _solution = Solution()
    inp = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in inp:
        print(_solution.largestPalindrome(i))

if __name__ == "__main__":
    main()
