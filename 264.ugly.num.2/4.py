#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321, C0326

class Solution(object):
    '''Solution description'''
    def func(self, n):
        '''Solution function description'''
        ugly = [1] * n
        i2 = i3 = i5 = -1
        x = v2 = v3 = v5 = 1
        for k in range(n):
            x = min(v2, v3, v5)
            ugly[k] = x
            if x == v2:
                i2 += 1
                v2 = ugly[i2] * 2
            if x == v3:
                i3 += 1
                v3 = ugly[i3] * 3
            if x == v5:
                i5 += 1
                v5 = ugly[i5] * 5
        return x

def main():
    '''main function'''
    _solution = Solution()
    inp = [1600]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
