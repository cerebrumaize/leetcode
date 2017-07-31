#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, n, k):
        '''Solution function description'''
        total = 1
        source_str = ''
        for i in range(1, n + 1):
            source_str += str(i)
            total *= i
        ret = ''
        k = k - 1
        for i in range(n):
            total = total//(n - i)
            index = k//total

            ret += source_str[index]
            temp_str = source_str[0: index] + source_str[index+1: len(source_str)]
            source_str = temp_str
            k = k%total
        return ret

def main():
    '''main function'''
    _solution = Solution()
    inp = [(3, 1)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
