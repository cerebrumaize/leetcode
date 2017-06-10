
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, n):
        '''
        Solution function description
        '''
        div, mod = divmod(n, 2)
        tmp = []
        for i in xrange(div, -1, -1):
            tmp.append((i, mod+(div-i)*2))
        print tmp
        res = 0
        for pair in tmp:
            res += (self.factor(pair[0]+pair[1])/(self.factor(pair[0])*self.factor(pair[1])))
        return res
    def factor(self, n):
        if n==0:return 1
        else: return n*self.factor(n-1)

def main():
    '''main function'''
    _solution = Solution()
    a = 1
    res = _solution.func(a)
    print res

if __name__ == "__main__":
    main()
