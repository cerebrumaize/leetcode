#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, t, s):
        '''Solution function description'''
        t = iter(t)
        return all(c in t for c in s)

def main():
    '''main function'''
    _solution = Solution()
    inp = [('jsofidjoajsodfijfoisajdisdfiaoisjdfijaposdjifoaisjgmsdflmx;lcvkpoeiwroqiwherdnxinxjnvlz;xcvkzx;lckfjowairjoewjr[qji', 'ojji'),\
           ('jsafoji', '')]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
