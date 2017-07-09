#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def removeKdigits(self, num, k):
        '''Solution function description'''
        if not k: return num
        if len(num) == k: return '0'
        res = []
        for c in num:
            #res里有值, 且不超过k个, 且栈顶比当前c大
            while k and res and res[-1] > c:
                #把所有比c大的都丢出去, 最多丢出去k个数
                res.pop()
                k -= 1
                print('while loop, ', res)
            res.append(c)
            print('for loop, ', res)
        return ''.join(res[:-k or None]).lstrip('0') or '0'

def main():
    '''main function'''
    _solution = Solution()
    inp = [('10', 1), ('10200', 1), ('10', 2)]
    for i in inp:
        print('result is', _solution.removeKdigits(i[0], i[1]))

if __name__ == "__main__":
    main()
