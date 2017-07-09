#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, t, s):
        '''Solution function description'''
        i, j, m, n = 0, 0, len(s), len(t)
        if not t: return True
        if m == n and s[0] != t[0]: return False
        while i < m and j < n:
            if s[i] == t[j]: j += 1
            i += 1
        return True if j == n else False

def main():
    '''main function'''
    _solution = Solution()
    inp = [('jsofidjoajsodfijfoisajdisdfiaoisjdfijaposdjifoaisjgmsdflmx;lcvkpoeiwroqiwherdnxinxjnvlz;xcvkzx;lckfjowairjoewjr[qji', 'ojji'),\
           ('jsafoji', '')]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
