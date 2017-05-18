
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, x):
        '''
        Solution function description
        '''
        if x > -10 and x < 10:
            return x
        l = str(abs(x))[::-1]
        ri = int(l)
        if ri > 2**31-1:
            return 0
        if x < 0:
            ri = -1 * ri
        return ri
def main():
    '''main function'''
    _solution = Solution()
    a = 123
    res = _solution.func(a)
    print res

if __name__ == "__main__":
    main()
