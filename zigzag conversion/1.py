import itertools as it

#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, s, numRows):
        '''
        Solution function description
        '''
        res = []
        for k in xrange(numRows):
            res.append([])
        for k in xrange(numRows):
            sub_i = k
            while sub_i < len(s):
                res[k].append(s[sub_i])
                sub_i += (2*numRows - 2)
        for k in xrange(2*numRows - 4, 0, -2):
            sub_i = numRows-1+k/2
            while sub_i < len(s):
                res[numRows-1-k/2].append(s[sub_i])
                sub_i += (2*numRows - 2)
        final_res = []
        for l in res:
            print l
            l1 = l[0:len(s)/(2*numRows)+2]
            l2 = l[len(s)/(2*numRows)+2:]
            l = [x+y for (x,y) in list(it.izip_longest(l1, l2, fillvalue=''))]
            print l
            final_res = final_res + l
        return ''.join(x for x in final_res)

def main():
    '''main function'''
    _solution = Solution()
    a = "0123456789ABCDEFGHIJKLMNOPQRST"
    b = 4
    res = _solution.func(a, b)
    print res

if __name__ == "__main__":
    main()
