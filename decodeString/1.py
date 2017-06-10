#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def helper(self, s, a, b):
        '''a is -1, b is -2'''
        n = len(s)
        return a * (1 if '0' not in s[-1:] else 0) + b * (1 if int(s[-2:]) <= 26 and '0' not in s[-2] else 0)
    def func(self, s):
        '''
        Solution function description
        '''
        if not s: return 0
        n = len(s)
        res = []
        if n >= 1: res.append(1 if int(s[0]) >=1 else 0)
        if n >= 2: 
          if s[:2][0] == '0': tmp = 0
          elif '0' not in s[:2] and int(s[:2]) <= 26: tmp = 2
          else: tmp = 1
          res.append(tmp)
        for i in range(2, n):
            temp = self.helper(s[:i+1], res[-1], res[-2])
            res.append(temp)
        print(res)
        return res[-1]

def main():
    '''main function'''
    _solution = Solution()
    a = ['', '12', '89', '129', '00', '456465132300684']
    for i in a:
      print(_solution.func(i))

if __name__ == "__main__":
    main()
