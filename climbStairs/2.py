
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, n):
        '''
        Solution function description
        '''
        if n==1: return 1
        prev1, prev2 = 1, 2
        for i in xrange(1, n):
          prev1, prev2 = prev2, prev1+prev2
        return prev1

def main():
    '''main function'''
    _solution = Solution()
    a = 7
    res = _solution.func(a)
    print res

if __name__ == "__main__":
    main()
